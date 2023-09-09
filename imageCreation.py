import openai
import requests
from PIL import Image
from io import BytesIO

# 将以下YOUR_API_KEY替换为您的OpenAI API密钥
# openai.api_key = "YOUR_API_KEY"
openai.api_key = os.getenv('OPENAI_API_KEY') 

# 输入您的自然语言描述
prompt = "可爱的小猫在草地上玩耍"

# 请求DALL-E生成图像
response = openai.Image.create(
    prompt=prompt,
    n=1,
    size="512x512",
    response_format="url"
)

# 获取图像URL
image_url = response['data'][0]['url']

# 下载并显示图像
image_data = requests.get(image_url).content
image = Image.open(BytesIO(image_data))
image.show()
