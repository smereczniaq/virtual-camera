# Virtual Camera

## Project Overview
The Virtual Camera project is designed to create a virtual camera in Python. It reads a scene from a `.txt` file and visualizes it. This project includes implementing a virtual camera and a Binary Space Partitioning (BSP) tree algorithm for hidden surface removal.

## Scene File Format
The `.txt` file format for the scene specifies vertices, edges, and faces as follows:
- **Vertices:** Defined by their coordinates (x, y, z).
- **Edges:** Defined by pairs of vertex indices.
- **Faces:** Defined by indices of edges forming the face.

Example:
```
-500, 200, 800 | -300, 200, 800 | -300, 200, 1000 | -500, 200, 1000 | -500, -200, 800 | -300, -200, 800 | -300, -200, 1000 | -500, -200, 1000;
0, 1 | 1, 2 | 2, 3 | 3, 0 | 4, 5 | 5, 6 | 6, 7 | 7, 4 | 0, 4 | 4, 7 | 7, 3 | 3, 0 | 1, 5 | 5, 4 | 4, 0 | 2, 6 | 6, 5 | 5, 1 | 3, 7 | 7, 6 | 6, 2;
0, 1, 2, 3 | 4, 5, 6, 7 | 8, 9, 10, 11 | 0, 12, 13, 14 | 1, 15, 16, 17 | 2, 18, 19, 20
```
## Features
1. **Virtual Camera Implementation**: Visualize scenes as defined in the `.txt` files.
2. **Hidden Surface Removal**: Implementing the BSP tree algorithm to manage and render only visible surfaces.

## Controls
The application allows user interaction through keyboard inputs to move and rotate the camera:

| Key           | Action                                             |
|---------------|----------------------------------------------------|
| `w`           | Move forward                                       |
| `s`           | Move backward                                      |
| `d`           | Move right                                         |
| `a`           | Move left                                          |
| `command`     | Move downward                                      |
| `space`       | Move upward                                        |
| `↑` (Up)      | Rotate clockwise along the horizontal (X) axis     |
| `↓` (Down)    | Rotate counterclockwise along the horizontal (X) axis |
| `←` (Left)    | Rotate counterclockwise along the vertical (Y) axis |
| `→` (Right)   | Rotate clockwise along the vertical (Y) axis       |
| `.` (Period)  | Rotate clockwise along the perpendicular (Z) axis  |
| `,` (Comma)   | Rotate counterclockwise along the perpendicular (Z) axis |

## Getting Started
To run the Virtual Camera, ensure you have Python installed and clone this repository. Navigate to the project directory and run the main script:<br>
`pip install -r requirements.txt`<br>
`python main.py`