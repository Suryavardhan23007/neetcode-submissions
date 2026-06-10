class Solution {

    public String encode(List<String> strs) {
        StringBuilder str = new StringBuilder();
        for(int i = 0; i < strs.size(); i++){
            String s = strs.get(i);
            for(int k = 0; k < s.length(); k++){
                str.append((int) s.charAt(k)).append('#');
            }
            str.append('&');
        }
        return str.toString();
    }

    public List<String> decode(String str) {
        List<String> lis = new ArrayList<>();
        StringBuilder s = new StringBuilder();
        StringBuilder word = new StringBuilder();

        for(char ch: str.toCharArray()){
            if (ch == '#'){
                word.append((char) Integer.parseInt(s.toString()));
                s.setLength(0);
                continue;
            }
            else if(ch != '&'){
                s.append(ch);
            }
            else if(ch == '&'){
                lis.add(word.toString());
                word.setLength(0);
            }

        }
        return lis;

    }
}
