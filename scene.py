from manim import *
import numpy as np

class Waves(Scene):
    def construct(self):

        # Parameters for SHM
        L = 1  # wavelength
        w0 = 3  # angular frequency
        A0 = 3  # amplitude
        ph = 0  # initial phase angle

        # Add an introductory slide
        text1 = Text(
            "Compilation of different Travelling Waves", 
            font_size=40, 
            color=GREEN
        )

        dq = MathTex(
            r"\lambda=1, \omega=3, A=3, \phi=0",
            font_size=36
        )


        equations = VGroup(text1,dq).arrange(DOWN, buff=0.5)
        self.play(Write(text1),
                  Write(dq),
        )
        self.play(FadeOut(text1,dq))
        self.wait(2)

        k=2*np.pi/L

        # Create the axes
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[-2, 2, 1],
            axis_config={"include_numbers": True},
        ).add_coordinates()

        # Add labels to the axes
        xl=r"x(t) = sin{(\omega x-kt)}"
        axes_labels = axes.get_axis_labels(x_label="x", y_label=xl)

        # Initial sine wave
        wave = axes.plot(lambda x: np.sin((w0*x)), color=BLUE)

        # Time tracker for the wave
        time_tracker = ValueTracker(0)

        # Update function for dynamic sine wave
        def update_wave(wave):
            wave.become(
                axes.plot(
                    lambda x: np.sin((w0*x - k*time_tracker.get_value())),
                    color=BLUE
                )
            )

        # Add the sine wave and axes
        self.play(Create(axes), Write(axes_labels))
        self.add(wave)

        # Make the sine wave dynamic
        wave.add_updater(update_wave)

        # Animate the time tracker to update the wave
        self.play(time_tracker.animate.increment_value(7), run_time=7, rate_func=linear)

        # Wait before ending
        self.wait()
        self.play(FadeOut(axes_labels, axes,wave))

        # Add labels to the axes
        xl=r"x(t) = cos{(\omega x + kt)}"
        axes_labels = axes.get_axis_labels(x_label="x", y_label=xl)

        # Initial sine wave
        wave = axes.plot(lambda x: np.cos((w0*x)), color=BLUE)

        # Time tracker for the wave
        time_tracker = ValueTracker(0)

        # Update function for dynamic sine wave
        def update_wave(wave):
            wave.become(
                axes.plot(
                    lambda x: np.cos((w0*x + k*time_tracker.get_value())),
                    color=BLUE
                )
            )

        # Add the sine wave and axes
        self.play(Create(axes), Write(axes_labels))
        self.add(wave)

        # Make the sine wave dynamic
        wave.add_updater(update_wave)

        # Animate the time tracker to update the wave
        self.play(time_tracker.animate.increment_value(7), run_time=7, rate_func=linear)

        # Wait before ending
        self.wait()
        self.play(FadeOut(axes_labels, axes,wave))

        # Create the axes
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[-2, 2, 1],
            axis_config={"include_numbers": True},
        ).add_coordinates()

        # Add labels to the axes
        xl=r"x(t) = e^{-(wx-kt)^2}"
        axes_labels = axes.get_axis_labels(x_label="x", y_label=xl)

        # Initial sine wave
        wave = axes.plot(lambda x: np.exp(-(w0*x)**2), color=BLUE)

        # Time tracker for the wave
        time_tracker = ValueTracker(0)

        # Update function for dynamic sine wave
        def update_wave(wave):
            wave.become(
                axes.plot(
                    lambda x: np.exp(-(w0*x - k*time_tracker.get_value())**2),
                    color=BLUE
                )
            )

        # Add the sine wave and axes
        self.play(Create(axes), Write(axes_labels))
        self.add(wave)

        # Make the sine wave dynamic
        wave.add_updater(update_wave)

        # Animate the time tracker to update the wave
        self.play(time_tracker.animate.increment_value(5), run_time=5, rate_func=linear)

        # Wait before ending
        self.wait()
        self.play(FadeOut(axes_labels, axes,wave))

        # Create the axes
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[-2, 2, 1],
            axis_config={"include_numbers": True},
        ).add_coordinates()

        # Add labels to the axes
        xl=r"x(t) = ln((x-t)^2+0.1)"
        axes_labels = axes.get_axis_labels(x_label="x", y_label=xl)

        # Initial sine wave
        wave = axes.plot(lambda x: np.log(((w0*x)**2)+0.1), color=BLUE)

        # Time tracker for the wave
        time_tracker = ValueTracker(0)

        # Update function for dynamic sine wave
        def update_wave(wave):
            wave.become(
                axes.plot(
                    lambda x: np.log(((w0*x - k*time_tracker.get_value())**2)+0.1),
                    color=BLUE
                )
            )

        # Add the sine wave and axes
        self.play(Create(axes), Write(axes_labels))
        self.add(wave)

        # Make the sine wave dynamic
        wave.add_updater(update_wave)

        # Animate the time tracker to update the wave
        self.play(time_tracker.animate.increment_value(5), run_time=5, rate_func=linear)

        # Wait before ending
        self.wait()
        self.play(FadeOut(axes_labels, axes,wave))

# Create the axes
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[-2, 2, 1],
            axis_config={"include_numbers": True},
        ).add_coordinates()

        # Add labels to the axes
        xl=r"x(t) = \frac{1}{1+e^-(\omega x - kt)} \text{(sigmoid function)}"
        axes_labels = axes.get_axis_labels(x_label="x", y_label=xl)

        # Initial sine wave
        wave = axes.plot(lambda x: 1/(1+np.exp((-(w0*x)))), color=BLUE)

        # Time tracker for the wave
        time_tracker = ValueTracker(0)

        # Update function for dynamic sine wave
        def update_wave(wave):
            wave.become(
                axes.plot(
                    lambda x: 1/(1+np.exp((-((w0*x)- k*time_tracker.get_value())))),
                    color=BLUE
                )
            )

        # Add the sine wave and axes
        self.play(Create(axes), Write(axes_labels))
        self.add(wave)

        # Make the sine wave dynamic
        wave.add_updater(update_wave)

        # Animate the time tracker to update the wave
        self.play(time_tracker.animate.increment_value(5), run_time=5, rate_func=linear)

        # Wait before ending
        self.wait()
        self.play(FadeOut(axes_labels, axes,wave))