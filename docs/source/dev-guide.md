# Developer Guide

## Developing New Objects
All objects, static and dynamic, derive from the BaseObject class. When creating a new object, you may either inherit directly from the BaseObject class or from an existing child class such as PedAgent or Vehicle.

### Color Visualization
The ObjectColors class defines all object colors for visualization when rendering in the grid. As desired, object colors can be changed or added.