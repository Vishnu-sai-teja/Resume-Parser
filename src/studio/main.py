import argparse
from agents.state import ResumeState

from agents.resume_reader import resume_reader
from agents.entity_extractor import entity_extractor
from agents.entity_validation import entity_validation
from agents.store_entities import store_entities
from agents.entity_corrector import correction_from_extractor

from langgraph.graph import StateGraph,START,END
from langgraph.checkpoint.memory import MemorySaver

file_path = "./data/VishnuSaiTeja_2025CV.pdf"


status = True # In future will be replaced with the actual status
def conditional_validation(state: ResumeState):
    global status
    print("\n\n\n",state['validated_entities'], "\n\n\n")
    if (len(state['validated_entities']) >=0) and (status == True):
        print("\n\nHey there + ", len(state['validated_entities']),"\n\n")
        status = False
        return "correction_from_extractor"
    else:
        return "store_entities" 

def build_graph():
    builder = StateGraph(ResumeState)
    builder.add_node('resume_reader', resume_reader)
    builder.add_node('entity_extractor', entity_extractor)
    builder.add_node('entity_validation', entity_validation)
    builder.add_node("store_entities", store_entities)
    builder.add_node("correction_from_extractor", correction_from_extractor)

    builder.add_edge(START, 'resume_reader')
    builder.add_edge('resume_reader', 'entity_extractor')
    builder.add_edge('entity_extractor', 'entity_validation')
    builder.add_conditional_edges('entity_validation', conditional_validation)
    builder.add_edge('correction_from_extractor','entity_validation')
    builder.add_edge('store_entities', END)

    return builder

# def process_resume(file_path: str):
memory = MemorySaver()  
builder = build_graph()
graph = builder.compile(interrupt_after=['resume_reader',
                                        'entity_extractor',
                                        'entity_validation',
                                        'correction_from_extractor',
                                        'store_entities',],
                        checkpointer=memory)

config = {
    "configurable" : {
        "thread_id": "2",
    }
}

initial_input = {
    "file_path": file_path,
    "current_stage": "START",
    "resume_text": "",
    "extracted_entities": {},
    "validated_entities": {},
    "errors": [],
    "interrupt": False,
    "feedback": {}
}

# def process_resume(file_path):
#     start = True
#     while True:
#         if start == True:
#             for event in graph.stream(initial_input, config, stream_mode="values"):
#                 start = False
#                 print("Continue....1")
#                 state = graph.get_state(config)
#         else :
#             for event in graph.stream(None, config, stream_mode="values"):
#                 print("Continue....2")

#         state = graph.get_state(config)
#         print(f"Current Stage : {state.values['current_stage']}")
#         if state.values['current_stage'] == "END":
#             break 

#         print("Interrupt......")
#         # try:
#         # for event in stream:
        
#         # feedback = input("Please provide your feedback or press Enter to continue: ")
#         # if feedback.lower() == 'quit':
#         #     return
#         state = state.values
#         update_state = {
#             "file_path": state['file_path'],
#             "resume_text": state['resume_text'],
#             "extracted_entities": state['extracted_entities'],
#             "validated_entities": state['validated_entities'],
#             "current_stage": state['current_stage'],
#             "errors": state['errors'],
#             "interrupt": state['interrupt'],
#             "feedback": ' '
#         }
#         print("current state : ", state)
#         while True:
#             action = input("\nEnter the state you want to modify, 'next' to proceed, or 'quit' to exit: ")

#             if action.lower() == 'quit':
#                 return
#             elif action.lower() == 'next':
#                 break
#             elif action in update_state.keys():
#                 print(f"Current value of {action}: {update_state[action]}")
#                 new_value = input(f"Enter new value for {action} (or press Enter to keep current value): ")
#                 if new_value:  # Only update if a new value is provided
#                     update_state[action] = new_value
#                     print(f"Updated {action} to: {new_value}")
#             else:
#                 print("Invalid state. Please try again.")
        
#         graph.update_state(config, update_state)

#             # if state['current_stage'] == END:
#             #     break

#         # except Exception as e:
#         #     print(f"Error processing resume: {str(e)}")
#         #     break


graph = build_graph().compile({"file_path": file_path})
# graph = build_graph().compile()

# for event in graph.stream(initial_input, config, stream_mode="values"):
#     state = graph.get_state(config)
#     if state.next != "__start__":
#         feedback = input("Please provide your feedback: ")
#         graph.update_state(config, { 
#             "file_path": state['file_path'],
#             "resume_text": state['resume_text'],
#             "extracted_entities": state['extracted_entities'],
#             "validated_entities": state['validated_entities'],
#             "current_stage": state['current_stage'],
#             "errors": state['errors'],
#             "interrupt": state['interrupt'],
#             "feedback": feedback})
    
# graph.invoke({
#     "file_path": '/Users/vishnusaitejanagabandi/Desktop/PIBIT Parser 2/src/data/VishnuSaiTeja_2025CV.pdf',
#     "current_stage" : "main"
# })

# graph.invoke({
#     "file_path": '/Users/vishnusaitejanagabandi/Desktop/PIBIT Parser 2/src/data/AkashGoel.docx',
#     "current_stage" : "main"
# })



