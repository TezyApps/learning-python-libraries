
def log_title(title: str) -> None:
    print(f"\n {title} ")
    print("=" * (len(title) + 4))

def log_body(body) -> None:
    print(body)
    print("-" * 35, end="\n\n")