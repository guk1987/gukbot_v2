import os
import dotenv
import logging
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from datetime import datetime

dotenv.load_dotenv()
bot_token = os.environ.get("SLACK_BOT_TOKEN")
app_token = os.environ.get("SLACK_APP_TOKEN")
bot_name = os.environ.get("BOT_NAME")

logging.basicConfig(level=logging.INFO)

app = App(token=bot_token)

# 모든 이벤트를 로깅하는 미들웨어
@app.middleware
def log_request(logger, body, next):
    logger.debug(f"Received event: {body}")
    return next()

# 일반 메시지 이벤트 처리
@app.message("")
def handle_message(message, say, logger):
    try:
        text = message.get('text', '').strip()
        user_id = message.get('user', '')
        channel_id = message.get('channel', '')
        timestamp = message.get('ts', '')

        # 타임스탬프를 사람이 읽을 수 있는 형식으로 변환
        readable_time = datetime.fromtimestamp(float(timestamp)).strftime('%Y-%m-%d %H:%M:%S')

        # 채널 이름 가져오기
        channel_info = app.client.conversations_info(channel=channel_id)
        channel_name = channel_info['channel']['name']

        # 사용자 정보 가져오기
        user_info = app.client.users_info(user=user_id)
        user_name = user_info['user']['real_name']

        logger.info(f"[{channel_name}][{readable_time}][{user_name}] : {text}")

        # 메시지가 '꾹꾹봇'으로 시작하는지 확인
        if text.startswith(bot_name):
            # '꾹꾹봇' 다음의 명령어 추출
            command = text[len(bot_name):].strip()
            logger.info(f"감지된 명령어: {command}")

            # 명령어 처리
            if command == "안녕":
                say("반갑습니다.")
                logger.info("'안녕' 명령어에 응답 완료")
            else:
                say(f"죄송합니다. '{command}' 명령어를 이해하지 못했습니다.")
                logger.info(f"알 수 없는 명령어: {command}")

    except Exception as e:
        logger.error(f"메시지 처리 중 에러 발생: {e}")

if __name__ == "__main__":
    handler = SocketModeHandler(app, app_token)
    
    handler.start()
