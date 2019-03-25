export default {
    categoryGetLevel(categoryId, categories, nowLevel = 0) {
        for (let i = 0; i < categories.length; i++) {
            let c = categories[i];
            if (c.id === categoryId) {
                if (c.fid !== 0) {
                    nowLevel++;
                    nowLevel = this.categoryGetLevel(c.fid, categories, nowLevel);
                    break;
                }
            }
        }
        return nowLevel;
    },
    categoryPrintLevel(level) {
        let c = '&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp';
        if (level) {
            return (c).repeat(level - 1) + '&nbsp&nbsp ● -- ';
        } else {
            return '● ';
        }

    }
};
