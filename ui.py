import gradio as gr
from utils import predict_image

def build_ui():
    with gr.Blocks() as demo:
        gr.Markdown("# 🍃 Tea Leaf Disease Classifier")
        gr.Markdown("Upload a tea leaf image and get the predicted disease class.")

        with gr.Row():
            image_input = gr.Image(type="pil", label="Upload Leaf Image")
            output_text = gr.Textbox(label="Prediction Result")

        gr.Button("Predict").click(
            fn=predict_image,
            inputs=image_input,
            outputs=output_text
        )

    return demo
