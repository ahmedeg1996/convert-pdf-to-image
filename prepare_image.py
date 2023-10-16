def PrepareImage(ImagePath):
    ListImages = []
    OrginalImage = ImagePath.resize((256,256))
    OrginalImage = np.asarray(OrginalImage)
    ListImages.append(OrginalImage)
    X = np.array(ListImages)
    return X