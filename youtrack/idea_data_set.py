from os import path

import requests
from tqdm import tqdm
import zipfile

from youtrack.idea_activity_manager import IdeaActivityManager
from youtrack.snapshot_strategy import SnapshotStrategy


def idea_2019_03_20_to_idea_2020_03_21(snapshot_manager=None):
    activities_file_path = "data/activities_2019_03_20_to_idea_2020_03_21.json"
    zip_file_path = activities_file_path + ".zip"
    if not path.exists(activities_file_path):
        _download_file('https://public.boxcloud.com/d/1/b1!mX51eb5QPdXpDFPEoM1wOyfa441V0rv-NNhfCfMcKmSpI8_FYBTVL8G0Cw6v8AFWQycH6gPaIXIRBeWRrg0jwuu6bPc9eiugc5K6h520bOk1Ji5VuT1lsSO3RuEC_EYntUL7ixqlF-vUObUZMVdy2J9Y5OPgfbTFrC5xjsJCPydhoDYOrf3QoJGrh77raaNmB4D10briv77_Ye6HdhvbDiCsdHZlAZd4c7Rsztt1q_lFm4G0NS78DALf_mCVObX6jENpr_clXe-mT77Vuy9UUT5mttQTn0FuVpY4Tx4een2qP8XU1zZwdO7Oo2M3BTvOFstfU3kV4qX7P89ikQ4K2py7Ao5ApvIUGrflExk9_jADJsR8zyZxovyh2ouuXkeVBbKw-s-N83pWZHmG-pqsXr63HVuWqHeEoSAdABAbIcH3BSE-gTUKSPGolnO57xHGgkByu3Jnw-qTOWdRqSWXV_xC0LDidscNaAmuqge2IxILA69UGmaJqDq5CRhqpd7W8XUzFYmDMlgYiGv45AD2umRhGM6UF-DhIcbk4Z1HYv289vAvNViTvNLdxSjS3_964uuFh_XFqnxPs-znXFubCEXbOWJE4vagIkzpLdgC2Quu6pe6JABULIOy6Z-5EFzSAyPcRD3GewWhoFY76qA-FMODNwnkB3NVBd2Gv8i4zhIT2uDCmD20pElRLfAyL_y1H_KCvQSMKIKNhoOJMaYtjLrYlr5UcRojJifFReOHtqZ6rIwFQf_L2p2N02NH7QReyNuBygDKirLKasLNmoxl3mFZaJ-sTgcfI8SnSACNQZBaHDQ4OEan47keQSFCe0kbzf0fD7NKQa5RZeYSwa7ENPVugX_zd0BPQL2n7m-FJAtn9WDnyUohpreyhWSPbv33ioi7XN3-Fea5rTWSO2w4YrZn8dGHbob-igGcwXTxmJWTlqD-6wfBn3exZRax1X_QMlvnT4F0mPLNqM8VPmhCpNXPyTQjnbsVLZ1u2t2Yn1knxlqAc5-39etK-FjAlv4gfCtCe-Z1sWCmWeQ0UsrAiRU0NhTE7AlnNzsqpSZ_z31CTUZKncpqKgtM1HTLNCb1rtY5W8PzvXvadjlL4TKYW861f0PY4-NsiGDwmRTz2HTYBVELJZiHIUhKhF-HIt5LU97ZYwqkQtY87K6dmONuBWDAYxdfE5imH7paoppgf7kwBwp5U3ptIv8xe1y3BDY7dlKwP_r6y70XoPGvFPFn5QtMojMaYlObvtsXdILPMYKDc9Fu5NvlhDOjA1AkQr6znnUMVKuJohqV6h7gMbduM1MZ/download', zip_file_path)
    if not path.exists(zip_file_path):
        raise Exception("Can't download issue activities")

    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall("data")

    if not path.exists(activities_file_path):
        raise Exception("Failed to unzip activities file")

    if snapshot_manager is None:
        snapshot_manager = SnapshotStrategy()
    activity_manager = IdeaActivityManager(snapshot_manager)
    activity_manager.load_issues_from_activities_file('data/activities_3d.json')
    return snapshot_manager.issues


def _download_file(url, destination_path):
    request = requests.get(url, stream=True)
    total_size = int(request.headers.get('content-length', 0))
    progress_indicator = tqdm(total=total_size, unit='iB', unit_scale=True)
    with open(destination_path, 'wb') as file:
        for data in request.iter_content(1024):
            progress_indicator.update(len(data))
            file.write(data)
    progress_indicator.close()
    if total_size != 0 and progress_indicator.n != total_size:
        print("error during downloading file {}".format(url))
