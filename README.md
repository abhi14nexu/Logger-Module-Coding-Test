# Logger-Module-Coding Design

The design for the project focuses on the principles of SOLID design as mentioned in the requirements. Following are some of hte key points about the design:

- **Single Responsibilities**: The design separates the responsibilities into distinct classes. The `LogFile` class handles file related operations, such as file creation,writiing, flushing, and checking for midnight rollover. The `LogComponent` class acts as a higher-level interface that utilizes the `LogFile` class to provide the overall logging functionality.

- **Interface-Based Design**: The `ILog` interface defines the public methods that the log component should expose which results into flexibility.

- **Modularity**: The design allows for easy extension and modification. Additional classes can be introduced to handle different log formats, log levels, or log destinations. By adhering to SOLID principles, the codebase remains modular and maintainable which makes it easy to add more functionalities and scaling in the future.

- **Unit Testing**: The design includes a separate unit test module that tests the log component's behavior. The unit tests cover the essential requirements, ensuring that the log component functions as expected, the unit tests are done using unittest framework (https://docs.python.org/3/library/unittest.html) for Python.

