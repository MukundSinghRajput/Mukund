<p align="center">
    <img src="https://te.legra.ph/file/ffdf379f4900afd32e518.jpg" width=312 height=312/>
    <br>
</p>

## Mukund: A Comprehensive Storage Handling Wrapper

In the ever-evolving landscape of software development, the efficient handling of data storage is a pivotal aspect of creating robust and scalable applications. One such storage handling wrapper that has gained prominence is Mukund. Let's explore the key features, design principles, and functionalities of Mukund, providing an in-depth understanding of its role in simplifying database interactions.

## Installing
Install and update using [pip](pypi.org):
```
$ pip install -U Mukund
```

### Origins and Purpose

Mukund is a JSON based storage handling wrapper designed to streamline database operations and provide a convenient interface for developers to interact with their data. Developed with simplicity and efficiency in mind, Mukund aims to empower developers by offering a user-friendly abstraction layer over traditional database interactions. The wrapper is particularly suited for applications that require persistent data storage and retrieval.

### Key Components

#### 1. Database Initialization

Mukund's initialization process begins with the creation of a database instance. Developers can instantiate Mukund by providing a unique name for the database. This simple yet crucial step establishes a connection to the storage location and sets the stage for subsequent interactions.

```
storage = Mukund("MukundX")
```

#### 2. Collection Management

One of Mukund's core functionalities is the management of collections within the database. Collections serve as containers for related data, and Mukund provides a seamless mechanism to create or access them.

```
col = mukund_instance.database("students")
```

The wrapper abstracts away the intricacies of handling individual collection files, allowing developers to focus on the logical organization of their data.

#### 3. Data Operations

Mukund supports various data operations, including insertion, retrieval, updating, and deletion. The Base class, part of Mukund's architecture, encapsulates these operations in a clean and modular fashion. For instance, adding a new key-value pair to a collection is as straightforward as calling the put method:

col.put("user_123", {"name": "Mukund", "age": 16, "email": "mukund@example.com"})

#### 4. Querying

To enhance flexibility, Mukund incorporates querying capabilities. Developers can specify conditions for filtering data, enabling targeted retrieval based on predefined criteria. The query method facilitates complex queries and supports regular expressions for matching values.

```
result_above_25 = col.query(condition_func=lambda col: col.get("age", 0) > 15)
```

### Design Principles

Mukund's design adheres to several key principles:

#### 1. Simplicity

The wrapper prioritizes simplicity in both its usage and underlying implementation. With a minimalistic and intuitive code, developers can quickly integrate Mukund into their projects without the need for extensive training.

#### 2. Extensibility

Mukund's design allows for easy extension and customization. The wrapper provides a solid foundation for developers to build upon, ensuring adaptability to diverse project requirements and future enhancements.

#### 3. Error Handling

Error handling is an integral part of Mukund's design philosophy. The wrapper employs informative error messages and exceptions to guide developers in identifying and resolving issues efficiently.


## A simple example 
```python 

from Mukund import Mukund 

storage = Mukund("MukundX")

collection = storage.database("users")
```

## Examples
See Example folder for examples

## Contact
- Updates : https://t.me/itzMukund
- Support : https://t.me/MukundChat
