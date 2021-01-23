from .pattern_hash_tbl import PATTERN_HASH_TBL, TABLE_NAME as PATTERN_HASH_TABLE_NAME
from .stub_tbl import STUB_TBL, TABLE_NAME as STUB_TABLE_NAME
from .call_logs_tbl import CALL_LOG_TABLE


DYNAMO_TABLES = [
    PATTERN_HASH_TBL,
    STUB_TBL,
    CALL_LOG_TABLE,
]
