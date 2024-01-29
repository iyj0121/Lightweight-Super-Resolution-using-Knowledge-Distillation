**About PyTorch 1.6.0**
  * Now the main branch supports PyTorch 1.6.0 by default.

# knowledge distillation을 활용한 EDSR-PyTorch모델 경량화

**About PyTorch 1.6.0**
  * feature map transfer 방식 등, KD에서 사용하는 방식으로 EDSR에 적용하여 모델 경량화 실험 진행

<img width="580" alt="스크린샷 2024-01-29 오후 9 50 02" src="https://github.com/iyj0121/DataBase_Project/assets/90498398/2044e07b-6c3c-4265-be0a-9c8527c1db43">

<img width="936" alt="스크린샷 2024-01-29 오후 9 50 14" src="https://github.com/iyj0121/DataBase_Project/assets/90498398/ef4c0659-dae1-4e4e-9195-6498083f6e7b">

This repository는 **"Enhanced Deep Residual Networks for Single Image Super-Resolution"** from **CVPRW 2017, 2nd NTIRE**.[here](https://github.com/LimBee/NTIRE2017) EDSR모델을 **"Paying More Attention to Attention: Improving the Performance of Convolutional Neural Networks via Attention Transfer"** from **ICLR2017: https://openreview.net/forum?id=Sks9_ajex** [here](https://arxiv.org/abs/1612.03928) 방식을 활용하여 모델 경량화를 진행하려고 한다.

<img width="687" alt="스크린샷 2023-05-18 오전 1 35 21" src="https://github.com/sanghyun-son/EDSR-PyTorch/assets/90498398/305aa921-23ea-449c-8974-e556c1e2cb4d">

중간 실험 결과
AT의 하이퍼파라미터를 1.0으로 했을 때, 결과. 오히려 지식 증류를 받은게 더 성능이 떨어짐.

<img width="681" alt="스크린샷 2023-05-18 오전 1 35 35" src="https://github.com/sanghyun-son/EDSR-PyTorch/assets/90498398/64e98b71-bf18-4b01-a802-4705e9aec223">

<img width="670" alt="스크린샷 2023-05-18 오전 1 35 53" src="https://github.com/sanghyun-son/EDSR-PyTorch/assets/90498398/c6e5a7eb-87b7-4aa7-b04c-f53e726a9699">

<img width="670" alt="스크린샷 2023-05-22 오후 9 53 37" src="https://github.com/sanghyun-son/EDSR-PyTorch/assets/90498398/56f524af-4d6a-4fc2-9399-2c9ba5adfe44">

최종 실험 결과

<img width="613" alt="최종결과" src="https://github.com/iyj0121/Junior-Project/assets/90498398/2ad8a281-a9cf-4d92-9838-abdae32b7ddd">

KD방식이 아닌 pruning 등 다른 방식으로 모델 경량화를 이어나갈 예정.

[1] Bee Lim, Sanghyun Son, Heewon Kim, Seungjun Nah, and Kyoung Mu Lee, **"Enhanced Deep Residual Networks for Single Image Super-Resolution,"** <i>2nd NTIRE: New Trends in Image Restoration and Enhancement workshop and challenge on image super-resolution in conjunction with **CVPR 2017**. </i> [[PDF](http://openaccess.thecvf.com/content_cvpr_2017_workshops/w12/papers/Lim_Enhanced_Deep_Residual_CVPR_2017_paper.pdf)] [[arXiv](https://arxiv.org/abs/1707.02921)] [[Slide](https://cv.snu.ac.kr/research/EDSR/Presentation_v3(release).pptx)]
```
@InProceedings{Lim_2017_CVPR_Workshops,
  author = {Lim, Bee and Son, Sanghyun and Kim, Heewon and Nah, Seungjun and Lee, Kyoung Mu},
  title = {Enhanced Deep Residual Networks for Single Image Super-Resolution},
  booktitle = {The IEEE Conference on Computer Vision and Pattern Recognition (CVPR) Workshops},
  month = {July},
  year = {2017}
}
@inproceedings{Zagoruyko2017AT,
    author = {Sergey Zagoruyko and Nikos Komodakis},
    title = {Paying More Attention to Attention: Improving the Performance of
             Convolutional Neural Networks via Attention Transfer},
    booktitle = {ICLR},
    url = {https://arxiv.org/abs/1612.03928},
    year = {2017}}
```

## Dependencies
* Python 3.6
* PyTorch >= 1.6.0
* numpy
* skimage
* **imageio**
* matplotlib
* tqdm
* cv2 >= 3.xx (Only if you want to use video input/output)

## Code
Clone this repository into any place you want.
```bash
git clone git@git.ajou.ac.kr:iyj0121/lightweight-super-resolution-using-knowledge-distillation.git
cd lightweight-super-resolution-using-knowledge-distillation
```

## Quickstart (Demo)
You can test our super-resolution algorithm with your images. Place your images in ``test`` folder. (like ``test/<your_image>``) We support **png** and **jpeg** files.

Run the script in ``src`` folder. Before you run the demo, please uncomment the appropriate line in ```demo.sh``` that you want to execute.
```bash
cd src       # You are now in */EDSR-PyTorch/src
sh demo.sh
```

You can find the result images from ```experiment/test/results``` folder.

You can evaluate your models with widely-used benchmark datasets:

[Set5 - Bevilacqua et al. BMVC 2012](http://people.rennes.inria.fr/Aline.Roumy/results/SR_BMVC12.html),

[Set14 - Zeyde et al. LNCS 2010](https://sites.google.com/site/romanzeyde/research-interests),

[B100 - Martin et al. ICCV 2001](https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/bsds/),

[Urban100 - Huang et al. CVPR 2015](https://sites.google.com/site/jbhuang0604/publications/struct_sr).

**Update log**
