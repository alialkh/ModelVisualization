import sys
sys.path.append('../')
from pycore.tikzeng import *

# defined your arch
arch = [
    to_head( '..' ),
    to_cor(),
    to_begin(),

    ##### would include input image here #####
#    to_input()

    # block 1
    to_Conv("conv11",'', '', offset="(0,0,0)", to="(0,0,0)", height=64, depth=64, width=1 ),
    to_Conv("conv12", '224x224', '', offset="(0,0,0)", to="(conv11-east)", height=64, depth=64, width=1 ),
    to_Pool("pool1", offset="(3,0,0)", to="(conv12-east)", height=32, depth=32, width=1),

    to_connection("conv12", "pool1"),    

    #block2
    to_Conv("conv21", '', '', offset="(0,0,0)", to="(pool1-east)", height=32, depth=32, width=2 ),
    to_Conv("conv22", '112x112', '', offset="(0,0,0)", to="(conv21-east)", height=32, depth=32, width=2 ),
    to_Pool("pool2", offset="(2,0,0)", to="(conv22-east)", height=16, depth=16, width=1),

    to_connection("conv22", "pool2"),

    #block3
    to_Conv("conv31", '', '', offset="(0,0,0)", to="(pool2-east)", height=16, depth=16, width=3 ),
    to_Conv("conv32", '', '', offset="(0,0,0)", to="(conv31-east)", height=16, depth=16, width=3 ),
    to_Conv("conv33", '64x64', '', offset="(0,0,0)", to="(conv32-east)", height=16, depth=16, width=3 ),
    to_Pool("pool3", offset="(2,0,0)", to="(conv33-east)",height=8, depth=8, width=1),

    to_connection("conv33", "pool3"),

    #block4
    to_Conv("conv41", '', '', offset="(0,0,0)", to="(pool3-east)", height=8, depth=8, width=4 ),
    to_Conv("conv42", '', '', offset="(0,0,0)", to="(conv41-east)", height=8, depth=8, width=4 ),
    to_Conv("conv43", '32x32', '', offset="(0,0,0)", to="(conv42-east)", height=8, depth=8, width=4 ),
    to_Pool("pool4", offset="(2,0,0)", to="(conv43-east)", height=4, depth=4, width=1),

    to_connection("conv43", "pool4"),

    #block5
    to_Conv("conv51", '', '', offset="(0,0,0)", to="(pool4-east)", height=4, depth=4, width=5 ),
    to_Conv("conv52", '', '', offset="(0,0,0)", to="(conv51-east)", height=4, depth=4, width=5 ),
    to_Conv("conv53", '16x16', '', offset="(0,0,0)", to="(conv52-east)", height=4, depth=4, width=5 ),
    to_Pool("pool5", offset="(2,0,0)", to="(conv53-east)", height=2, depth=2, width=1),

    to_connection("conv53", "pool5"),

    #block6
    to_Conv("conv6", '', '', offset="(0,0,0)", to="(pool5-east)", height=2, depth=2, width=8 ),

    
    #block6 upsample
    to_UnPool("block6Up", caption="16x16",  offset="(2,0,0)", to="(conv6-east)", height=4,depth=4,width=1),
    
    to_connection("conv6","block6Up"),

    #block5 upsample
    to_UnPool("block5Up", caption="",  offset="(2,0,0)", to="(block6Up-east)", height=8,depth=8,width=1),

    #block 4 has a convolution then upsampling by factor of 
    to_Conv("conv4Up",'','', offset="(2,0,0)", to="(block5Up-east)", height=4,depth=4,width=5),
    to_UnPool("block4Up", caption="",  offset="(0,0,0)", to="(conv4Up-east)", height=8,depth=8,width=1),
    to_skip('pool4', 'conv4Up', pos="2.0"),

    #block 2 conv then upsampling ### MUST CONNECT THIS TO BLOCK 3 UPSAMPLING ### 
    to_Conv("conv2Up",'','', offset="(2,0,0)", to="(block4Up-east)", height=16,depth=16,width=5),
    to_UnPool("block2Up", caption="",  offset="(0,0,0)", to="(conv2Up-east)", height=32,depth=32,width=1),
    
    to_Conv("conv1Up",'','', offset="(4,0,0)", to="(block2Up-east)", height=32,depth=32,width=5),
    to_UnPool("block1Up", caption="",  offset="(0,0,0)", to="(conv1Up-east)", height=64,depth=64,width=1),



 #   to_Conv("conv2", 128, 64, offset="(1,0,0)", to="(pool3-east)", height=32, depth=32, width=2 ),
 #   to_Pool("pool2", offset="(0,0,0)", to="(conv2-east)", height=28, depth=28, width=1),
 #   to_SoftMax("soft1", 10 ,"(3,0,0)", "(pool1-east)", caption="SOFT"  ),
 #   to_connection("pool2", "soft1"),
    to_end()
    ]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()
