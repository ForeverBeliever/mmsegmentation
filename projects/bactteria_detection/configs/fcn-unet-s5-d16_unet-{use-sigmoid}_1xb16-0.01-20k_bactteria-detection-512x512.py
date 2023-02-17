_base_ = [
    'mmseg::_base_/models/fcn_unet_s5-d16.py',
    './bactteria-detection_512x512.py', 'mmseg::_base_/default_runtime.py',
    'mmseg::_base_/schedules/schedule_20k.py'
]
custom_imports = dict(imports='datasets.bactteria-detection_dataset')
img_scale = (512, 512)
data_preprocessor = dict(size=img_scale)
optimizer = dict(lr=0.01)
optim_wrapper = dict(optimizer=optimizer)
model = dict(
    data_preprocessor=data_preprocessor,
    decode_head=dict(
        num_classes=2, loss_decode=dict(use_sigmoid=True), out_channels=1),
    auxiliary_head=None,
    test_cfg=dict(mode='whole', _delete_=True))
vis_backends = None
visualizer = dict(vis_backends=vis_backends)
work_dir = 'projects/bactteria_detection/work_dirs/fcn-unet-\
    s5-d16_unet-{use-sigmoid}_1xb16-\
    0.01-20k_bactteria-detection-512x512/'
