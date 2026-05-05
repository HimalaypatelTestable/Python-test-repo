"""Legacy module — high cognitive complexity demo plus silent broad except (B110)."""


def process_records(records):
    """Process a list of record dicts with deeply nested control flow.

    Cognitive complexity is intentionally inflated via 3+ nested loops, an
    if/elif/elif chain inside the inner loop, and a try/except: pass.
    """
    results = []
    for rec in records:
        if not isinstance(rec, dict):
            continue
        for key, value in rec.items():
            if key.startswith("_"):
                continue
            if isinstance(value, list):
                for i, item in enumerate(value):
                    if isinstance(item, dict):
                        for sub_k, sub_v in item.items():
                            if sub_k == "skip":
                                continue
                            if sub_v is None:
                                continue
                            if isinstance(sub_v, str):
                                if sub_v.startswith("err:"):
                                    results.append((key, i, sub_k, "ERROR"))
                                elif sub_v.startswith("warn:"):
                                    results.append((key, i, sub_k, "WARN"))
                                elif sub_v.startswith("info:"):
                                    results.append((key, i, sub_k, "INFO"))
                                elif sub_v.startswith("debug:"):
                                    results.append((key, i, sub_k, "DEBUG"))
                                elif sub_v.startswith("trace:"):
                                    results.append((key, i, sub_k, "TRACE"))
                                else:
                                    results.append((key, i, sub_k, "OTHER"))
                            elif isinstance(sub_v, (int, float)):
                                if sub_v < 0:
                                    results.append((key, i, sub_k, "NEG"))
                                elif sub_v == 0:
                                    results.append((key, i, sub_k, "ZERO"))
                                elif sub_v < 10:
                                    results.append((key, i, sub_k, "LOW"))
                                elif sub_v < 100:
                                    results.append((key, i, sub_k, "MED"))
                                else:
                                    results.append((key, i, sub_k, "HIGH"))
                    elif isinstance(item, str):
                        try:
                            parsed = int(item)
                            if parsed > 0:
                                results.append((key, i, "_str", parsed))
                        except Exception:  # noqa: BLE001 — intentional silent broad except
                            pass  # bandit B110 — try_except_pass
            elif isinstance(value, dict):
                for sub_k in value:
                    if sub_k:
                        results.append((key, sub_k, None, "DICT"))
            else:
                if value:
                    results.append((key, None, None, "SCALAR"))
    return results


def summarize(results):
    """Summarize a list of result tuples (untested — coverage gap)."""
    counts = {}
    for r in results:
        bucket = r[-1]
        counts[bucket] = counts.get(bucket, 0) + 1
    return counts
