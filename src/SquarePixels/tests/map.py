import pygame
from pygame.locals import *
from OpenGL.GL import *
import numpy as np

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
pygame.display.set_caption("Stylized Map")

# Shaders
vertex_shader = """
    #version 330
    in vec2 position;
    out vec4 fragPosition;
    void main()
    {
        gl_Position = vec4(position, 0.0, 1.0);
        fragPosition = gl_Position;
    }
"""

fragment_shader = """
precision highp float;
precision highp sampler2D;

in vec2 position;  // Changed from varying vec2 vUv;

uniform vec3 fog_color;
uniform float fog_density;
uniform float time;
uniform float turbulence_scale;
uniform float pressure;
uniform int pressure_iteration;

void main () {
    vec2 coord = position - pressure * texture2D(uTexture, position).xy;  // Changed from vUv
    gl_FragColor = pressure * texture2D(uTexture, coord);
    gl_FragColor.a = 1.0;

    // Apply pressure iteration
    for (int i = 0; i < pressure_iteration; i++) {
        vec2 divergence = texture2D(uTexture, position).xy;  // Changed from vUv
        vec2 gradient = -0.5 * vec2(
            texture2D(uTexture, position - vec2(1.0, 0.0)).x - texture2D(uTexture, position + vec2(1.0, 0.0)).x,
            texture2D(uTexture, position - vec2(0.0, 1.0)).y - texture2D(uTexture, position + vec2(0.0, 1.0)).y
        );

        vec2 laplacian = texture2D(uTexture, position - vec2(1.0, 0.0)).xy +
                         texture2D(uTexture, position + vec2(1.0, 0.0)).xy +
                         texture2D(uTexture, position - vec2(0.0, 1.0)).xy +
                         texture2D(uTexture, position + vec2(0.0, 1.0)).xy -
                         4.0 * texture2D(uTexture, position).xy;

        vec2 newVelocity = pressure * gradient + pressure * laplacian - divergence;
        coord = position - newVelocity;

        // Apply dissipation
        gl_FragColor = pressure * texture2D(uTexture, coord);
        gl_FragColor.a = 1.0;
    }
}
"""

# Compile shaders
shader_program = glCreateProgram()
vertex_shader_object = glCreateShader(GL_VERTEX_SHADER)
glShaderSource(vertex_shader_object, vertex_shader)
glCompileShader(vertex_shader_object)
fragment_shader_object = glCreateShader(GL_FRAGMENT_SHADER)
glShaderSource(fragment_shader_object, fragment_shader)
glCompileShader(fragment_shader_object)
glAttachShader(shader_program, vertex_shader_object)
glAttachShader(shader_program, fragment_shader_object)
glLinkProgram(shader_program)
glUseProgram(shader_program)


# Function to draw rectangles
def draw_rectangles(rect_list, color, time, turbulence_scale, pressure, use_fog=False):
    glUniform3f(glGetUniformLocation(shader_program, "color"), *color)
    glUniform3f(glGetUniformLocation(shader_program, "fog_color"), 0.7, 0.7, 0.7)
    glUniform1f(
        glGetUniformLocation(shader_program, "fog_density"), 5.0
    )  # Not using fog density for this example
    glUniform1f(glGetUniformLocation(shader_program, "time"), time)
    glUniform1f(
        glGetUniformLocation(shader_program, "turbulence_scale"), turbulence_scale
    )
    glUniform1f(glGetUniformLocation(shader_program, "pressure"), pressure)

    glBegin(GL_QUADS)
    for rect in rect_list:
        glUniform2f(glGetUniformLocation(shader_program, "position"), rect[0], rect[1])
        glVertex2f(rect[0], rect[1])
        glVertex2f(rect[0] + rect[2], rect[1])
        glVertex2f(rect[0] + rect[2], rect[1] + rect[3])
        glVertex2f(rect[0], rect[1] + rect[3])
    glEnd()


# Main function
def main():
    # Sample data (replace this with your own data)
    map_rect = [(0.0, 0.0, 1.0, 1.0)]  # Represents the entire map
    land_rects = [(0.1, 0.1, 0.2, 0.2), (0.4, 0.4, 0.3, 0.2)]
    unexplored_rects = [(0.5, 0.2, 0.15, 0.15), (0.3, 0.7, 0.18, 0.12)]

    clock = pygame.time.Clock()
    time = 0.0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Draw background (entire map)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_rectangles(
            map_rect, (0.0, 0.0, 0.0), time, turbulence_scale=0.1, pressure=2.0
        )

        # Draw land and unexplored areas with shaders
        draw_rectangles(
            land_rects, (0.0, 1.0, 0.0), time, turbulence_scale=0.1, pressure=2.0
        )
        draw_rectangles(
            unexplored_rects,
            (0.0, 0.0, 0.0),
            time,
            turbulence_scale=0.1,
            pressure=2.0,
            use_fog=True,
        )

        pygame.display.flip()
        pygame.time.wait(10)
        time += 0.01
        clock.tick(60)


if __name__ == "__main__":
    main()
