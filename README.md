## Multi-Threaded Priority Message Queue Implementation

This project implements a multi-threaded priority message queue system where multiple threads can send messages to each other with varying priorities. Additionally, upon receiving a message, the receiving thread performs a simple action using a thread pool.

### Assignment Description
In this assignment, the primary objectives are:
1. Implement a priority message queue data structure supporting enqueue, dequeue, peek, and empty check operations.
2. Create a thread pool with a fixed number of threads.
3. Implement message sending between threads with specified priorities.
4. Upon message reception, perform a simple action using the thread pool.
5. Test the implementation with multiple threads sending messages to each other with different priorities.

### Implementation Overview
- **UserThread Class**: Represents a user thread with functionalities to send and receive messages.
- **Message Queue Operations**: Functions for enqueue, dequeue, peek, and checking if the queue is empty.
- **Message Handler**: Manages incoming messages and dispatches them to respective threads.
- **Thread Pool**: A fixed thread pool for executing simple actions upon message reception.

### Usage
To run the implementation:
1. Install the `dankware` package using `pip install -U dankware` (used for pretty colors in the console).
2. Run the `main.py` file.
3. Provide the number of threads/users when prompted.
4. The system will simulate message exchanges between threads with different priorities.
5. Upon completion, the program will shut down gracefully.

### Example
Here's a brief example of how to use the system:

```python
# Example usage
# Enqueue messages with different priorities
threads['T1'].send_msg('T2', 1, 'Hey T2, how ya been?') # lowest priority
threads['T1'].send_msg('T3', 2, 'Long time no see, T3!')
threads['T3'].send_msg('T1', 3, 'Been a while T1, hope you\'re well :)') # highest priority

# Additional examples...
# Sending a message to oneself
threads['T1'].send_msg('T1', 1, 'I am talking to myself (clearly delulu)')
```

### Output
The program will display the following output in the console:

```
  - [T3]>[T1]: Been a while T1, hope you're well :)
  - [T1]>[T3]: Long time no see, T3!
  - [T1]>[T2]: Hey T2, how ya been?
  - [T1] I am talking to myself (clearly delulu)
```

## Architecture and Design Documentation

### Overview
The Multi-Threaded Priority Message Queue Implementation is designed to facilitate communication between multiple threads with varying priorities. The system comprises several key components working together seamlessly to ensure efficient message handling and execution of associated actions.

### Components

1. **UserThread Class**
   - Represents a user thread within the system.
   - Handles sending and receiving messages.
   - Each thread has its inbox for incoming messages.

2. **Message Queue**
   - Data structure supporting priority-based message queuing.
   - Operations include enqueue, dequeue, peek, and empty check.
   - Messages are stored with their respective priorities.

3. **Message Handler**
   - Responsible for managing incoming messages.
   - Dispatches messages to the appropriate threads based on priorities.
   - Ensures thread safety during message processing.

4. **Thread Pool**
   - Fixed pool of threads for executing simple actions upon message reception.
   - Ensures concurrency and parallel execution of actions.
   - Utilizes ThreadPoolExecutor from the concurrent.futures module.

### Design Considerations

- **Priority-Based Queue**: Messages are stored in the queue based on their priority level to ensure timely processing of high-priority messages.
  
- **Thread Safety**: Implementation is designed to handle concurrent access to the message queue and thread interactions safely, preventing race conditions and deadlocks.

- **Scalability**: The system's design allows for scalability by adjusting the number of threads in the thread pool to accommodate increased workload and message traffic.

- **Efficiency**: Optimization techniques such as sleep intervals and efficient data structures are employed to minimize resource utilization and maximize throughput.

### Workflow

1. **Initialization**: The system initializes by creating user threads and starting the message handler thread.

2. **Message Sending**: Threads can send messages to each other by specifying the receiver, priority, and message content.

3. **Message Reception**: Upon receiving a message, the message handler dispatches it to the appropriate thread based on priority.

4. **Action Execution**: The receiving thread executes a predefined action using the thread pool upon message reception.

5. **Completion**: The system gracefully shuts down after completing message exchanges and processing.

### Future Improvements

- **Enhanced Error Handling**: Implement robust error handling mechanisms to gracefully handle exceptions and edge cases.
  
- **Dynamic Thread Pool**: Introduce dynamic resizing of the thread pool based on workload and system resources.

- **Extended Functionality**: Incorporate additional features such as message acknowledgment, message expiration, and message filtering.

### Conclusion

The Multi-Threaded Priority Message Queue Implementation provides a robust framework for inter-thread communication with prioritized message handling. By leveraging a combination of thread management, message queuing, and action execution, the system ensures efficient and reliable message processing in multi-threaded environments.

For detailed code implementation, refer to the source code.

### License
This project is licensed under the [MIT License](LICENSE).
