from langchain.agents import Tool
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI
import os
from webSearch import getContent #搜索工具
from esStore import getHistory,getmeans ##获取辅助信息
#进行提示工程，并调用自己做的工具。   在langchain整合的基础上
    #根据问题来生成promot
    #使用分词器划分句义，NLTK（Natural Language Toolkit）：NLTK是一个流行的Python库，提供了多种文本处理和NLP功能。
    # 它包含了分词器（Tokenizer）和词性标注器（Part-of-Speech Tagger）等工具，可以帮助你将句子分解成单词，并提供词语的一些基本含义信息。
    #es根据词语解释意思，没匹配就不解释
    #重新构造问题
    #2、根据问题，检索出相关历史对话作为参考
    #3、调用搜索引擎，检索出帮助信息
    #构造promot
    #调用chatgpt的api
s="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"
def getAnswer(question):
    llm=OpenAI(temperature=0,openai_api_key="sJ",openai_proxy='http://127.0.0.1:7890')
    tools = [
    Tool(
        name="搜索",
        func=getContent,
        description="它对于在线获取有关用户问题的相关信息很有帮助"
    ),
    Tool(
        name="语义分析",
        func=getmeans,
        description="它对于理解句子中某些词的隐含意思很有帮助"
    ),
    Tool(
        name="上下文关联",
        func=getHistory,
        description="它对于获取与问题相关的之前的对话上下文很有帮助"
    )
    ]
    agent=initialize_agent(tools,llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,verbose=True)
    result=agent.run(question)
    return result
    
    