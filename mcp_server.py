import sys
import json
from client import EarleyParser

def main():
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        req = json.loads(line)
        method = req.get("method")
        params = req.get("params", {})
        if method == "parse":
            parser = EarleyParser(params.get("grammar", {}))
            ok = parser.parse(params.get("tokens", []))
            res = {"accepted": ok}
        else:
            res = {"error": "unknown method"}
        sys.stdout.write(json.dumps({"id": req.get("id"), "result": res}) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
