from .pattern_hash_tbl import PATTERN_HASH_TBL, TABLE_NAME as PATTERN_HASH_TABLE_NAME
from .stub_tbl import STUB_TBL, TABLE_NAME as STUB_TABLE_NAME, STUB_TBL_SECONDARY_INDEX
from .call_logs_tbl import CALL_LOG_TABLE

# this is used by the create_tables script
DYNAMO_TABLES = [
    (PATTERN_HASH_TBL, None),
    (STUB_TBL, STUB_TBL_SECONDARY_INDEX),
    (CALL_LOG_TABLE, None),
]
