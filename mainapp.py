import streamlit as st
import time

# Set the page config
st.set_page_config(page_title="Greet User Fun", layout="centered")

# Display the app header
st.header("Fun Greeting App")

# Ask for the user's name
name = st.text_input("What's your name?")

if name:
    # Placeholder for dynamic content
    placeholder = st.empty()

    # Display a fun and dynamic greeting
    greeting_styles = [
        f"<h1 style='color: red;'>Hello, {name}!</h1>",
        f"<h1 style='color: blue;'>Hello, {name}!</h1>",
        f"<h1 style='color: green;'>Hello, {name}!</h1>",
        f"<h1 style='color: purple;'>Hello, {name}!</h1>",
        f"<h1 style='color: orange;'>Hello, {name}!</h1>",
        f"<h1 style='font-size: 24px;'>Hello, {name}!</h1>",
        f"<h1 style='font-size: 32px;'>Hello, {name}!</h1>",
        f"<h1 style='font-size: 40px;'>Hello, {name}!</h1>",
        f"<h1 style='font-style: italic;'>Hello, {name}!</h1>",
        f"<h1 style='text-decoration: underline;'>Hello, {name}!</h1>"
    ]

    for style in greeting_styles:
        placeholder.markdown(style, unsafe_allow_html=True)
        time.sleep(0.5)  # Pause for half a second

    # Display a final static greeting
    placeholder.markdown(f"<h1>Hello, {name}!</h1>", unsafe_allow_html=True)
else:
    st.write("Please enter your name above to see the magic.")


# test
pip install biopython

from Bio.Seq import Seq
from Bio.SeqUtils import GC

def dna_operations(dna_sequence):
    """
    Performs various operations on a DNA sequence: transcription, translation,
    and calculating GC content.

    :param dna_sequence: A string representing the DNA sequence.
    """
    dna = Seq(dna_sequence)

    # Transcription: DNA -> RNA
    rna = dna.transcribe()

    # Translation: RNA -> Protein
    protein = rna.translate()

    # Calculate GC Content
    gc_content = GC(dna)

    # Print the results
    print(f"DNA Sequence: {dna}")
    print(f"RNA Sequence (Transcription): {rna}")
    print(f"Protein Sequence (Translation): {protein}")
    print(f"GC Content: {gc_content:.2f}%")

# Example usage with a sample DNA sequence
if __name__ == "__main__":
    sample_dna_sequence = "ATGCTACGATCGATCGATACGATCGTAGCTAGCTAGCTAGCTAGCTGAC"
    dna_operations(sample_dna_sequence)
