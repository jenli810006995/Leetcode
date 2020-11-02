'''
referred to https://blog.csdn.net/MrJustin/article/details/105650123

'''

class Solution {
    public List<List<String>> displayTable(List<List<String>> orders) {
        Set<String> items = new HashSet<>();
        Map<Integer, Map<String, Integer>> tableOfFood = new HashMap<>();
        
        for(List<String> order: orders){
            String customerName = order.get(0), foodItem = order.get(2);
            items.add(foodItem);
            int tableNumber = Integer.valueOf(order.get(1));
            if(!tableOfFood.containsKey(tableNumber)) tableOfFood.put(tableNumber, new HashMap());
            tableOfFood.get(tableNumber).put(foodItem, tableOfFood.get(tableNumber).getOrDefault(foodItem, 0)+1);
        }
        
        List<String> firstRow = new ArrayList<>();
        firstRow.addAll(items);
        Collections.sort(firstRow);
        
        List<List<String>> res = new ArrayList<>();
        Map<Integer, Map<String, Integer>> treeMap = new TreeMap<>(tableOfFood);
        
        for (Map.Entry<Integer, Map<String, Integer>> entry : treeMap.entrySet()) {
            List<String> list = new ArrayList<>();
            Map<String, Integer> table = entry.getValue();
            list.add(String.valueOf(entry.getKey()));
            for(String s: firstRow){
                if(table.containsKey(s)) list.add(String.valueOf(table.get(s)));
                else list.add("0");
            }
            res.add(list);
        }
        firstRow.add(0, "Table");
        res.add(0, firstRow);
        
        return res;
    }
}
