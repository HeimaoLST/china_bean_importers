import subprocess
import sys


def test_beangulp_importers_do_not_load_removed_legacy_ingest():
    subprocess.run(
        [sys.executable, "-c", "from china_bean_importers.beangulp import wechat, alipay_mobile, cmb_debit_card"],
        check=True,
    )
