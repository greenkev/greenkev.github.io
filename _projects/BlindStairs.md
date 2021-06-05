---
title: "Blind Stair Traversal via Reinforcement Learning"
excerpt: "Research Project lead by [Jonah Seikmann](https://twitter.com/JonahSiekmann) to train reactive control policies to scale staircases without perception.<br/><img src='/images/BlindStairsPreview.jpg'>"
collection: portfolio
date: 2021-05-01 00:00:00
---

Looking to the future, highly successful legged robots will operate alongside humans autonomously while using perception, such as lidar and cameras. These sensors are getting cheaper and smaller over time. Mapping algorithms are getting better and computationally cheaper. This raises the question, why should we care about work on control methods that don't use perception for rough or varying terrain?
To quote Prof. Bill Smart "All sensors are terrible," they are all "noisy, late, and wrong." No sensor will every be perfect. They will improve over time but the algorithms and control methods that use their data must be robust to their noise, latency and systematic error. 

<img src='/images/BlindStairs.jpg'>

[In this RSS paper](https://arxiv.org/abs/2011.04741), instead of working within the context of a specific perception system we sought to identify and construct a walking controller for Cassie which can scale stairs without any information at all. Then future researchers can build off of these methods to include world estimate information to improve the robot's robustness and capabilities. Additionally, we can analyze the emergent behavior that the controller learns to teach us about the physics of locomotion.

This work is incredibly similar to Jonah and Yesh’s previous ICRA paper [“Sim-to-Real Learning of All Common Bipedal Gaits via Periodic Reward Composition.”](https://arxiv.org/abs/2011.01387) In fact, it shares the same learning algorithm (PPO), periodic force/velocity reward function and model of the robot. The core difference is the randomization of the environment. Simply by carefully designing a series of random staircases for the robot to climb and descend in training we were able to create a control policy that was wildly successful at climbing stairs in the real world. The ranges of parameters we varied are shown in the figure below, more details can be found in the paper.

<img src='/images/StairDiagram.png'>

The resulting control policy can be seen in the video below. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/MPhEmC6b6XU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


