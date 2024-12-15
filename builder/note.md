### Builder Design Pattern: Key Concepts

The **Builder Design Pattern** is a **creational pattern** that provides a way to construct complex objects step by step. It separates the construction process from the representation, allowing you to create different representations of an object using the same construction code.

#### Key Concepts:
- **Builder**: Defines an abstract interface for creating parts of a product.
- **Concrete Builder**: Implements the Builder interface to construct and assemble parts of the product.
- **Director**: Oversees the construction process using a Builder object.
- **Product**: The final object that is constructed.

#### Advantages:
- Makes object creation clear and manageable.
- Allows the construction process to vary independently of the product’s representation.
- Supports the creation of immutable objects.

#### Example:
For constructing a **car**:
- The **Builder** defines the steps like `addWheels`, `addEngine`, etc.
- A **Concrete Builder** specifies how these steps are implemented for, say, a sports car or a truck.
- The **Director** manages the steps to build a complete car.
- The **Product** is the final car object.

This pattern is useful when:
- You need to construct objects with multiple configurations.
- Object creation involves several steps that can be combined in different ways.