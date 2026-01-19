"""
Funções utilitárias para criação e manipulação de strings.
"""

import os
import threading
from datetime import datetime


__all__ = [
    'now_pid_tid_str',
]


_TIMESTAMP_FMT = "%Y%m%d-%H%M%S-%f"


def now_pid_tid_str() -> str:
    """
    Retorna uma string com timestamp atual, PID e TID.

    O formato é:
        YYYYMMDD-HHMMSS-ffffff-pid<PID>-tid<TID>

    Útil para nomes de arquivos, logs e identificação
    de eventos concorrentes.
    """
    timestamp = datetime.now().strftime(_TIMESTAMP_FMT)
    pid = os.getpid()
    tid = threading.get_ident()

    return f"{timestamp}-pid{pid}-tid{tid}"
