from dotenv import load_dotenv
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback


def main():
    load_dotenv()
    st.set_page_config(page_title="Enter details")
    st.header("Enter your details 💬")
    
    with st.form(key = "Info"):
          st.write("Inside the form")
          name=st.text_input(label = "Enter the your name")
          nric=st.text_input(label = "Enter the nric ")
          option = st.selectbox(
        "Gender?",
        ("Male", "Female"))
    
    # gender=my_form.text_input(label = "Enter the gender ")
          dob=st.date_input("Date of birth", value=None)
    
          submit = st.form_submit_button(label="submit", help="Click to submit!")
    
    if submit:
      # st.write(submit)
      if name and nric and option and dob :
              st.success(
                            f"ID:  \n Hello  {name}  \n NRIC: {nric}  \n Gender: {option} \n  \n DoB: {dob} "
                        )
                 
      file1 = open("info_1.txt","r")
      file2 = open("info_2.txt","r")
      file3 = open("info_3.txt","r")
      file4 = open("info_4.txt","r")
      file5=  open("info_5.txt","r")
      congrat= open("congrat.txt","r")
      # st.write("Hi "+name)
      
      if(nric.endswith('4')):
        #  st.write(congrat.read())
         st.write(file4.read())
      elif(nric.endswith('3')):
        # st.write(congrat.read())
        st.write(file3.read())
      elif(nric.endswith('2')):
        # st.write(congrat.read())
        st.write(file2.read())
      elif(nric.endswith('1')):
        # st.write(congrat.read())
        st.write(file1.read())
      else:
        st.write(file5.read())
 
      
    # upload file
    pdf = st.file_uploader("Upload your PDF document", type="pdf")
    
    # extract the text
    if pdf is not None:
      pdf_reader = PdfReader(pdf)
      text = ""
      for page in pdf_reader.pages:
        text += page.extract_text()
        
      # split into chunks
      text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
      )
      chunks = text_splitter.split_text(text)
      
      # create embeddings
      embeddings = OpenAIEmbeddings()
      knowledge_base = FAISS.from_texts(chunks, embeddings)
      
      # show user input
      user_question = st.text_input("Ask a question about your PDF:")
      if user_question:
        docs = knowledge_base.similarity_search(user_question)
        
        llm = OpenAI()
        chain = load_qa_chain(llm, chain_type="stuff")
        with get_openai_callback() as cb:
          response = chain.run(input_documents=docs, question=user_question)
          print(cb)
           
        st.write(response)
    

if __name__ == '__main__':
    main()
