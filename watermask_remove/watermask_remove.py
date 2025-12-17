import cv2
import numpy as np
from PIL import Image

def remove_watermark_high_fidelity(input_path, output_path, watermark_roi):
    """
    高保真去除图片水印
    :param input_path: 输入图片路径（支持jpg/png）
    :param output_path: 输出图片路径
    :param watermark_roi: 水印区域坐标 (x1, y1, x2, y2)，即左上角和右下角坐标
    """
    # 1. 读取图像（保留原始通道和分辨率）
    img = cv2.imread(input_path, cv2.IMREAD_UNCHANGED)
    if img is None:
        raise ValueError("无法读取图片，请检查路径或文件格式")
    
    # 2. 创建水印掩码（掩码区域为白色，其余黑色）
    mask = np.zeros(img.shape[:2], dtype=np.uint8)
    x1, y1, x2, y2 = watermark_roi
    mask[y1:y2, x1:x2] = 255  # 水印区域标记为白色
    
    # 3. 图像修复（INPAINT_TELEA算法兼顾保真和修复效果）
    # INPAINT_NS 更注重细节，INPAINT_TELEA 修复速度更快，可根据需求切换
    repaired_img = cv2.inpaint(
        img, 
        mask, 
        inpaintRadius=3,  # 修复半径（适配小水印）
        flags=cv2.INPAINT_TELEA
    )
    
    # 4. 保存修复后的图像（无压缩，保留原始质量）
    # PNG用无损压缩，JPG设置质量100
    if output_path.lower().endswith('.jpg') or output_path.lower().endswith('.jpeg'):
        cv2.imwrite(output_path, repaired_img, [cv2.IMWRITE_JPEG_QUALITY, 100])
    else:
        cv2.imwrite(output_path, repaired_img, [cv2.IMWRITE_PNG_COMPRESSION, 0])
    
    print(f"水印已去除，结果保存至: {output_path}")
    return repaired_img

# ==================== 核心参数配置 ====================
if __name__ == "__main__":
    # 替换为你的图片路径
    INPUT_IMAGE_PATH = "cover.png"   # 输入图片（如原图片路径）
    OUTPUT_IMAGE_PATH = "cover_no_watermark.png"  # 输出无水印图片
    
    # 水印区域坐标（需根据实际水印位置调整，示例为右下角"豆包AI生成"的大致区域）
    # 可通过画图工具/PS查看水印的x1,y1（左上角）和x2,y2（右下角）
    WATERMARK_ROI = (2166, 1557, 2451, 1609)  # 示例坐标，需根据实际图片微调
    
    # 执行去除水印
    try:
        remove_watermark_high_fidelity(
            input_path=INPUT_IMAGE_PATH,
            output_path=OUTPUT_IMAGE_PATH,
            watermark_roi=WATERMARK_ROI
        )
    except Exception as e:
        print(f"处理失败: {str(e)}")