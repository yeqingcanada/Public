document.addEventListener('DOMContentLoaded', function () {
    const list = document.getElementById('list');
    let itemCount = 0;
    let isLoading = false;

    // 初始加载一些列表项
    loadMoreData();

    // 滚动事件监听
    list.addEventListener('scroll', function () {
        if (list.scrollTop + list.clientHeight >= list.scrollHeight - 10) {
            loadMoreData();
        }
    });

    function loadMoreData() {
        if (isLoading) return;
        isLoading = true;

        // 模拟从服务器获取数据
        setTimeout(() => {
            for (let i = 0; i < 20; i++) {
                const item = document.createElement('div');
                item.className = 'item';
                item.textContent = `列表项 ${itemCount++}`;
                list.appendChild(item);
            }
            isLoading = false;
        }, 1000);
    }
});
