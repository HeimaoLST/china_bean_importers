from importlib import import_module

__all__ = [
    "alipay_mobile",
    "alipay_web",
    "boc_credit_card",
    "boc_debit_card",
    "ccb_debit_card",
    "ccb_credit_card",
    "cmb_debit_card",
    "cmbc_credit_card",
    "cmbc_debit_card",
    "icbc_credit_card",
    "icbc_debit_card",
    "hsbc_hk",
    "thu_ecard_old",
    "webank_debit_card",
    "wechat",
]


def __getattr__(name):
    # Beancount 3 removes ingest; only load legacy importers when requested.
    if name in __all__:
        module = import_module(f"{__name__}.{name}")
        globals()[name] = module
        return module
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
