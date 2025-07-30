import sys
from ruamel.yaml import YAML

# 스크립트 실행 시 전달받은 인자 (새로운 태그, 파일 경로)
new_tag = sys.argv[1]
file_path = sys.argv[2]

yaml = YAML()
# ruamel.yaml이 YAML 포맷을 최대한 그대로 유지하도록 설정
yaml.preserve_quotes = True
yaml.indent(mapping=2, sequence=4, offset=2)

# YAML 파일 읽기
with open(file_path, "r") as f:
    data = yaml.load(f)

# 값 수정 (예: frontend.image.tag)
data["frontend"]["image"]["tag"] = new_tag

# 수정한 내용으로 파일 다시 쓰기
with open(file_path, "w") as f:
    yaml.dump(data, f)

print(f"Successfully updated {file_path} with tag: {new_tag}")
