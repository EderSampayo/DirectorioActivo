import argparse
from datetime import datetime, timedelta
import pandas as pd
import numpy as np

def convertir_timestamp(timestamp_100ns):
    timestamp_seconds = timestamp_100ns / 1e7
    timestamp_seconds -= 11644473600    # Desplazamiento (segundos entre la fecha 01/01/1601 y 1/01/1970)

    datetime_np = np.datetime64(int(timestamp_seconds), 's')
    df = pd.DataFrame({'Fecha': [datetime_np]})

    print(df)


def main():
    parser = argparse.ArgumentParser(description="Convertir timestamp de 100ns a fecha y hora")
    parser.add_argument('-f', '--timestamp_100ns', type=int, required=True, help="Valor")

    args = parser.parse_args()
    convertir_timestamp(args.timestamp_100ns)

if __name__ == "__main__":
    main()