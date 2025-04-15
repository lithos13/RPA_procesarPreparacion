"""In Python, a context object is a general term used to describe an object that holds information or state that is shared across different parts of an application or a specific scope. It is often used to manage 
   and pass around data that multiple functions or classes need access to, without relying on global variables.

Common Use Cases of Context Objects
Application Contexts: In frameworks like Flask, a context object is used to store information about the current request, user session, or application configuration.
Thread or Task Contexts: Context objects can store data specific to a thread or task, ensuring that the data is isolated and not shared across threads.
Custom Contexts: Developers can create their own context objects to encapsulate shared state or configuration for a specific part of their application. """
import pandas as pd

class general:
    bol_systemException = False
    df_transactionData  = pd.DataFrame()
    df_dataConfig      = pd.DataFrame()
    int_transactionNumber = 0
    row_transactionItem = None
    int_numRetry = 0
    int_totalRetry = 0
    str_messageError = ""