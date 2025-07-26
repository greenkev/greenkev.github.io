---
title: "Digit Locomotion"
excerpt: "Pushed forward the performance and reliability of Digit's locomotion. <br/><img src='/images/DigitStepRecovery.jpg' width='70%'>"
collection: portfolio
date: 2025-05-01 00:00:00
---

At Agility Robotics my work covers many aspects and methods of locomotion.

One very visible project I lead is the deployment of the first learned locomtion policy to a robot performing paid labor.
This specifically is a learned step recovery policy which is described briefly in [this agility blog post](https://www.agilityrobotics.com/content/crossing-sim2real-gap-with-isaaclab).
I worked together with Jonah Siekmann on training the first policy before taking over the training process myself.
I then worked through the realtime C++ integration of the policy into the behavior, planning, and control stack.
To make a convincing argument about the utility I build comprehensive simulation benchmarking tools and performed a large amount of hardware testing myself.

This work cumulated in it as a default feature in our internal released software. It prevented quite a few falls at the 2025 promat tradeshow demo. The robustness of these policies are showed off in the video below.

<iframe width="560" height="315" src="https://www.youtube.com/embed/2amzGvk97GE?si=rtVbsvvivmQu5axo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


Less visibly, I worked with one other software engineer to fully replace our model-based locomotion planner.
This was a challenging project in system design, work allocation, and high performance requirements.
The new system was a significant deviation, changing trajectory optimization tooling, dynamic model, objectives and constraints.
We built it to the point were it was equal or better in all scenarios then switched over all digits to use the new system.
Unfortunately, I can't go into too much more detail but I am very proud of the work.