import os
from llama_index.core import SimpleDirectoryReader
from llama_index.core.bridge.pydantic import BaseModel, Field
from llama_index.core.program import MultiModalLLMCompletionProgram
from llama_index.multi_modal_llms.openai import OpenAIMultiModal
from typing import List, Optional

# Read images
image_path = "./data"
image_documents = SimpleDirectoryReader(image_path).load_data()

# Desired output structure (Pydantic Program)
class PaperCard(BaseModel):
    """Data class for storing text attributes of a PaperCard."""
    title: str = Field(description="Title of paper.")
    year: str = Field(description="Year of publication of paper.")
    authors: str = Field(description="Authors of paper.")
    arxiv_id: str = Field(description="Arxiv paper id.")
    main_contribution: str = Field(
        description="Main contribution of the paper."
    )
    insights: str = Field(
        description="Main insight or motivation for the paper."
    )
    main_results: List[str] = Field(
        description="The main results of the paper."
    )
    tech_bits: Optional[str] = Field(
        description="Describe what's being displayed in the technical bits section of the image."
    )

paper_card_extraction_prompt = """
Use the attached PaperCard image to extract data from it and store into the provided data class.
"""

openai_mm_llm = OpenAIMultiModal(
    model="gpt-4o",
    api_key="REPLACE_THIS_WITH_YOUR_OPENAI_API_KEY",
    max_new_tokens=4096
)

program = MultiModalLLMCompletionProgram.from_defaults(
        output_cls=PaperCard,
        prompt_template_str=paper_card_extraction_prompt,
        multi_modal_llm=openai_mm_llm
    )

for doc in image_documents: 
    print("File name: " + os.path.basename(doc.image_path))
    print(program(image_documents=[doc]))
    print()
