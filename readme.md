# Image text extraction from PaperCards

This data extraction example uses OpenAI's multimodal Large Language Model (LLM) "gpt-4o" to extract and summarise information (structured data extraction) from so-called PaperCards. These are visualisations containing summaries of research papers. The `data` folder contains 35 PaperCards.

You need an OpenAI API key for this project. [Get your OpenAI API key here](https://platform.openai.com/login). You can insert your OpenAI API key in the `extract.py` script as `api_key`, or you can supply your OpenAI API key either via the `.env` file, or through an environment variable called `OPENAI_API_KEY`.

For example, from this PaperCard

![alt text](https://github.com/botextractai/ai-image-extraction/assets/159737833/475d93e9-dcfe-4905-8d42-7c219054cefe "Prometheus: Inducing Fine-Grained Evaluation Capability In Language Models")

the LLM will automatically extract this text:

```
File name: w47_2023-prometheus.excalidraw.png
title='Prometheus: Inducing Fine-Grained Evaluation Capability In Language Models' year='2023' authors='Kim, Seungone et al.' arxiv_id='arxiv:2310.08441' main_contribution='An open-source LLM (LLaMA2) evaluation specializing in fine-grained evaluations using feedback rubrics.' insights='While large LLMs have shown impressive performance, they still lack fine-grained evaluation capabilities. Prometheus aims to address this by
using feedback rubrics to provide more detailed evaluations.' main_results=['Prometheus matches or outperforms GPT-4.', 'Prometheus achieves better performance on 3 fine-grained evaluation tasks: MT Bench, Feedback Bench, and LLM Bar Exam.', 'Prometheus can function as a reward model.', 'Reference answers are crucial for fine-grained evaluations.'] tech_bits='Score Rubric, Feedback Collection, Generated Instructions, Generated Responses, Evaluations, Answers & Explanations'
```
