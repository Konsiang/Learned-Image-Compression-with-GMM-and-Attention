# Learned-Image-Compression-with-GMM-and-Attention
### Environment 

* Python==3.6.4

* Tensorflow==1.14.0

* [RangeCoder](https://github.com/lucastheis/rangecoder)

```   
    pip3 install range-coder
```

* [Tensorflow-Compression](https://github.com/tensorflow/compression) ==1.2

```
    pip3 install tensorflow-compression or 
    pip3 install tensorflow_compression-1.2-cp36-cp36m-manylinux1_x86_64.whl
```

### Test Usage

* Download the pre-trained [models](https://drive.google.com/open?id=19b92ey1g30R2OvWupekLQNb3TjHs5HLX) (this model is optimized by MS-SSIM using lambda = 14) and unzip it.

* Put your images to the directory valid/ and run the py files


```
    python3 encoder.py
```
```
    python3 decoder.py
```

* For JPEG Compression, run

```
    python3 JPEG_encoder.py
```
```
    python3 JPEG_decoder.py
```
## Notes

This implementations are not original codes of our CVPR2020 paper, because original code is based on Tensorflow 1.9.0 and many features have been removed. This repo is a re-implementation, but the core codes are almost the same and results are also consistent with original results. This repo is also submitted to CVPR Workshop and Challenge on Leanred Image Challenge ([CLIC] (http://www.compression.cc/)) with the entry Kattolab in the Leaderboard.

If you think it is useful for your reseach, please cite our CVPR2020 paper. Our original RD data in the paper is contained in the folder RDdata/.
```
@inproceedings{cheng2020image,
    title={Learned Image Compression with Discretized Gaussian Mixture Likelihoods and Attention Modules},
    author={Cheng, Zhengxue and Sun, Heming and Takeuchi, Masaru and Katto, Jiro},
    booktitle= "Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)",
    year={2020}
}
```



