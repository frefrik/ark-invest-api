from datetime import datetime


def _fmt(obj: dict):
    for k, v in obj.items():
        if isinstance(v, dict):
            _fmt(v)
        else:
            if "_pct" in k:
                obj[k] = {"raw": v, "fmt": _fmt_pct(v)}
            else:
                try:
                    obj[k] = {"raw": v, "fmt": human_format(v)}
                except Exception:
                    obj[k] = v

    return obj


def _fmt_pct(value):
    return f"{value:.2f}%"


def human_format(num):
    num = float("{:.6g}".format(num))
    magnitude = 0

    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    num = round(num, 2)

    ret_str = "{}{}".format(
        "{:f}".format(num).rstrip("0").rstrip("."), ["", "K", "M", "B", "T"][magnitude]
    )

    return ret_str


def _format_data(obj, dates={}):
    for k, v in obj.items():
        print(k, v)
        if k in dates:
            if isinstance(v, dict):
                obj[k] = v.get("fmt", v)
            elif isinstance(v, list):
                try:
                    obj[k] = [item.get("fmt") for item in v]
                except AttributeError:
                    obj[k] = [
                        datetime.fromtimestamp(date).strftime("%Y-%m-%d %H:%M:S")
                        for date in v
                    ]
            else:
                try:
                    obj[k] = datetime.fromtimestamp(v).strftime("%Y-%m-%d %H:%M:%S")
                except (TypeError, OSError):
                    obj[k] = v
        elif isinstance(v, dict):
            if "raw" in v:
                obj[k] = v.get("raw")
            elif "min" in v:
                obj[k] = v
            else:
                obj[k] = _format_data(v, dates)
        elif isinstance(v, list):
            if len(v) == 0:
                obj[k] = v
            elif isinstance(v[0], dict):
                for i, list_item in enumerate(v):
                    obj[k][i] = _format_data(list_item, dates)
            else:
                obj[k] = v
        else:
            obj[k] = v

    return obj


def weight_rank(df):
    df = df.sort_values(by="weight", ascending=False).reset_index(drop=True)
    df["weight_rank"] = df.index + 1

    return df
