escaped_str = input("이스케이프된 문자열을 입력하세요: ")

# 문자열을 바이트로 변환
byte_str = bytes(escaped_str.encode('utf-8').decode('unicode_escape'), 'latin1')

# 바이트를 UTF-8로 디코딩하여 한국어로 변환
decoded_str = byte_str.decode('utf-8')

print("디코딩된 문자열:", decoded_str)