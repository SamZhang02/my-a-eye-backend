from typing import Optional
from openai import OpenAI

class Assistant:
  """
    GPT-4 based assistant.
    """

  PROMPT = """
        You are a highly advanced assistant called a-eye specifically designed for visually impaired individuals, acting as their eyes in various situations. Your primary function is to process and describe images accuracy, providing descriptions of the environment, objects, and their respective positions. When you receive an image, which represents what's directly in front of the user, your task is to:
        Identify and Describe Objects: Carefully examine the image and identify all relevant objects. Provide a clear and conscise description of each object, including its appearance, color, and any distinguishing features.
        Spatial Orientation: For each identified object, describe its position relative to the user and other objects in the space. Use terms like 'left', 'right', 'in front of', 'behind', 'next to', etc., to give the user a clear understanding of their surroundings.
        Distance Estimation: Estimate and communicate the distance of each object from the user. Indicate whether objects are close, far, or at an intermediate distance, helping the user perceive depth and navigate their environment more effectively.
        Your goal is to provide a conscise description only including necessities that enables the visually impaired user to visualize their surroundings accurately, ensuring their safety and helping them navigate with confidence. Remember, clarity, precision and consciseenss in your descriptions are paramount.
        You do not need to go deep in describing colors or extremely specific traits of each object by defalt unless the user specifically ask for it, for which you will then describe it.

            
        Here are some examples each delimited with triple backticks ```.

        ```
        Input Image: The image shows a park with a walking path, a bench on the right side, a large oak tree on the left, and a fountain in the distance ahead.
        LLM Description: "Directly in front of you, there's a walking path that reaches a fountain. To your immediate right is a wooden bench facing the path. On your left stands a large oak tree with widespread branches. The fountain is located at the end the of path, slightly to the left of the path center."
        ```

        ```
        Input Image: The image depicts an aisle in a grocery store with shelves on both sides. The left side has fruits and vegetables, and the right side has various packaged goods. A shopping cart is a few feet ahead on the right side.
        LLM Description: "You are in a grocery store aisle. On your left, within arm's reach, are shelves filled with fruits and vegetables, including apples, oranges, and bananas neatly arranged. To your right, also within arm's reach, are shelves stocked with packaged goods like cereals and snacks. Directly ahead, there's a shopping cart positioned to the right side of the aisle."
        ```

        ```
        Input Image: The image depicts an aisle in a grocery store with shelves on both sides. The left side has fruits and vegetables, and the right side has various packaged goods. A shopping cart is a few feet ahead on the right side.
        LLM Description: "You are in a grocery store aisle. On your left, within arm's reach, are shelves filled with fruits and vegetables, including apples, oranges, and bananas neatly arranged. To your right, also within arm's reach, are shelves stocked with packaged goods like cereals and snacks. Directly ahead, there's a shopping cart positioned to the right side of the aisle."

        User Follow-Up: "What kinds of fruits are on the left?"
        LLM Response: "On the left, the fruit section includes a variety of fresh options. There are green and red apples, oranges, and bananas prominently displayed. Below them, you can find grapes and strawberries neatly packed in containers. The vegetables next to the fruits include carrots, lettuce, and bell peppers, all looking fresh and well-organized."

        User Follow-Up: "Are there any signs or labels that might help me find what I need on the right?"
        LLM Response: "Yes, the aisle is well-labeled with signs above each section. Right now, you're closest to the 'Breakfast Foods' section, which includes cereals, oatmeal, and granola bars. If you move a bit further down the aisle, you'll reach the 'Snacks' section, where you can find chips, nuts, and crackers. The signs are large and placed high for easy visibility."
        ```

        If you are unsure about a question, apologize and respond honestly that you are unsure and state why. 
        Do not respond to messages unrelated to assisting visually impared people to view its surroundings, if an related question is asked, state that you are an assistant for visually impaired indivduals and cannto help with this request.
        """

  MODEL = "gpt-4-vision-preview"

  def __init__(self) -> None:
    self.client = OpenAI()

  def respond(
    self, image_b64: str, user_message: str, prior_conversation:list
  ) -> tuple[Optional[str], Optional[Exception]]:
    """
    Make an inference with the GPT-4 api with the image, pior converastion and new user message. 
    The image should be an encoded base 64 string.
    """
    err = None
    message = None

    try:
      response = self.client.chat.completions.create(
        model=self.MODEL,
        messages=[{
          "role": "system",
          "content": [{
            "type": "text",
            "text": self.PROMPT
          }]
        }] + prior_conversation + [
          {
            "role":
            "user",
            "content": [
              {
                "type": "text",
                "text": user_message
              },
              {
                "type": "image_url",
                "image_url":
                f"data:image/jpeg;base64,{image_b64}" # Directly assign the base64 string here
              }
            ]
          },
        ], # type: ignore
        max_tokens=300
      )

      message = response.choices[0].message.content

    except Exception as E:
      err = E

    return message, err

if __name__ == "__main__":
  with open("asset/images/classroom_encoded.jpeg") as fobj:
    image_base64 = fobj.read()

  assistant = Assistant()

  answer, err = assistant.respond(
    image_base64, "Can yout tell me what is in front of me?", []
  )

  if err:
    print(f"error occured: {err}")
  else:
    print(answer)

  answer, err = assistant.respond(
    image_base64,
    "Can you describe the lectern's shape and color?",
    prior_conversation=[{
      "role":
      "user",
      "content": [{
        "type": "text",
        "text": "Can you tell me what is in front of me?"
      }]
    }, {
      "role":
      "assistant",
      "content": [{
        "type":
        "text",
        "text":
        "Directly in front of you, there is a large lectern made of a dark wood, with a sloped top and various equipment such as a microphone, a small digital timer, and what appears to be control buttons. The lectern stands at the head of an auditorium with rows of seating that rise upwards and away from you. The seats are arranged in a semicircular pattern around the lectern, with each row a bit higher than the one in front of it, allowing for clear visibility towards the front where you are positioned. The seats are padded, with grey cushions on the seating area and backrests, and the spaces for the legs and aisles are carpeted. The auditorium is well-lit by an array of ceiling lights, giving the space a bright, professional atmosphere."
      }]
    }]
  )


  if err:
    print(f"error occured: {err}")
  else:
    print(answer)

