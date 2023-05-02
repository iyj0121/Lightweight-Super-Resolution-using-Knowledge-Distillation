import torch

import utility
import data
import model
import loss
from option import args
from trainer import Trainer

from loss import at

torch.manual_seed(args.seed)
checkpoint = utility.checkpoint(args)

check = utility.checkpoint(args)

teacher_model = model.Model(args, check)
teacher_model.load_state_dict(torch.load('/home/iyj0121/EDSR-PyTorch/experiment/EDSR_x2.pt'), strict=False)
teacher_model.eval()

def main():
    global model
    if args.data_test == ['video']:
        from videotester import VideoTester
        model = model.Model(args, checkpoint)
        t = VideoTester(args, model, checkpoint)
        t.test()
    else:
        if checkpoint.ok:
            loader = data.Data(args)
            _model = model.Model(args, checkpoint)
            _loss = loss.Loss(args, checkpoint) if not args.test_only else None
            kd_loss = at.AT(p=2.0)
            t = Trainer(args, loader, _model, _loss, checkpoint, teacher_model, kd_loss)
            while not t.terminate():
                t.train()
                t.test()

            checkpoint.done()

if __name__ == '__main__':
    main()
