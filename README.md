# BatchCrypt

This is the source repo for paper ATC'20 paper "BatchCrypt: Efficient Homomorphic Encryption for Cross-Silo Federated Learning"

## Structure

FATE_plugin contains our patch to FATE 1.0.1
accuracy_eval contains our scripts to validate and evaluate our quantization and batching scheme for Homomorphic Encryption


## Background

Federated Learning: Federated learning is a machine learning approach where the model is trained collaboratively on decentralized data without centralized data aggregation.

Since Federated Learning is a fairly new ML technique, it has a lot of issues that arise along with it like the following:
- Data Privacy and Security: Federated learning relies on decentralized data stored on individual devices, raising concerns about data privacy, security, and potential vulnerabilities during data transmission and aggregation.
- Heterogeneity of Devices: Devices participating in federated learning may have different hardware capabilities, network conditions, and data distributions, making it difficult to ensure fairness and compatibility across the federated network.
- Model Aggregation Challenges: Combining locally trained models from various devices into a global model can be complex, as the models may have different update frequencies, quality, or divergent training objectives.
- Lack of Centralized Control: The absence of a centralized authority or control over the training process can make it challenging to monitor and manage the federated learning system, ensuring model integrity and preventing malicious behavior.


We are trying to tackle Privacy as an issue to Federated Learning. 

Homomorphic Encryption: Homomorphic encryption is a cryptographic technique used in federated learning to allow secure computation on encrypted data, enabling the central server to perform operations on encrypted model updates received from the participating devices without decrypting them, thus preserving data privacy.

Problem with Homomorphic Encryption: While homomorphic encryption offers a promising solution for preserving data privacy in federated learning, it also faces certain challenges that make it infeasible or impractical in certain scenarios. 
- Computational Overhead: Homomorphic encryption operations can be computationally intensive and require significant computational resources, resulting in slower execution compared to traditional computations on unencrypted data. The performance overhead can be a major bottleneck, especially for large-scale federated learning systems with numerous participants and complex models.
- Communication Overhead: Homomorphic encryption requires encrypted data to be transmitted between the central server and participating devices. This introduces additional communication overhead due to the increased size of encrypted data, potentially causing network congestion and latency issues.
- Limited Functionality: Homomorphic encryption schemes typically support a limited set of mathematical operations that can be performed on encrypted data. Complex machine learning algorithms often involve a wide range of operations beyond the capabilities of existing homomorphic encryption schemes, limiting the practicality of using this technique in federated learning.


Our aprocach aims to make Homomorphic Encryption feasible so that it becomes adaptable in places where we can make a trade off when it comes to accuracy and time taken and this system would help in applications where it is necessary to preserve the privacy of the system, take less time and let go of a little accuracy drop if it occurs. 

Our Approach: We are trying to reduce the time taken in model training. The approach is called 'Selective Layer Encryption'. When we encrypt models in this system, we build models based on the dataset, and put all the necessary layers in the model that will enhance the Privacy of the model and give the most accuarte training and testing results. Our system uses tensorflow for model training and the paillier cryptosystem for encryption and decryption. Now, maximum overhead is caused because there are layers that are important to make the system more accurate, but in turn take a lot of time to encrypt. So we go ahead and analyse what these layers are that, if removed will not take a toll on the accuracy, but reduce the time taken significantly. Now we need to analyse this based on what dataset it is that we are working on. For example, in image datasets, only the CNN Layers, Dense Layers and Activation layers are the most important layers and carry the most amount of information so we go ahead and encrypt just those. 

This results in the accuracy being almost the same, time taken dropping to more than 50% of what it took previously. 

Note: This setup was experimented with 2 datasets, FashionMNIST and CIFAR10. The layers that were selected in the selective layer encryption process were 60% of the original amount of layers, thus giving us the trade off for tima taken and accuracy along with privacy maintained. 
