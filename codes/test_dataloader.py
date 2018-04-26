import torchvision.utils
from data import create_dataloader, create_dataset

opt = {}
# # subset and HR path only
# opt['name'] = 'ImageNet'
# opt['dataroot_HR'] = '/mnt/SSD/xtwang/ImageNet_train'
# opt['dataroot_LR'] = None
# opt['subset_file'] = '/mnt/SSD/xtwang/BasicSR/ImageNet_list.txt'

# # HR path only
# opt['name'] = 'DIV2K800'
# opt['dataroot_HR'] = '/mnt/SSD/xtwang/BasicSR/DIV2K800_sub'
# opt['dataroot_LR'] = None
# opt['subset_file'] = None

# HR path and LR path
opt['name'] = 'DIV2K'
opt['dataroot_HR'] = '/mnt/SSD/xtwang/BasicSR_datasets/DIV2K800/DIV2K800_sub'
opt['dataroot_LR'] = '/mnt/SSD/xtwang/BasicSR_datasets/DIV2K800/DIV2K800_sub_bicLR'
opt['subset_file'] = None
opt['dataroot_ref'] = '/mnt/SSD/xtwang/BasicSR_datasets/ISO/fusion_merge_bicLRx2_100'
opt['reverse'] = True
opt['data_type'] = 'img'
opt['mode'] = 'LRHRref'
opt['phase'] = 'train'
opt['use_shuffle'] = True
opt['n_workers'] = 3
opt['batch_size'] = 64
opt['HR_size'] = 128
opt['scale'] = 4
opt['use_flip'] = True
opt['use_rot'] = True

train_set = create_dataset(opt)
train_loader = create_dataloader(train_set, opt)

for i, data in enumerate(train_loader):
    print(i)
    LR = data['LR']
    HR = data['HR']
    ref = data['ref']
    torchvision.utils.save_image(LR, 'LR_{:03d}.png'.format(i), nrow=8, padding=2, normalize=False)
    torchvision.utils.save_image(HR, 'HR_{:03d}.png'.format(i), nrow=8, padding=2, normalize=False)
    torchvision.utils.save_image(ref, 'ref_{:03d}.png'.format(i), nrow=8, padding=2, normalize=False)