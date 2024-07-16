from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello_world():
    return "<div style='background:lightgreen'><h1>My Flask story</h1><br><p>In a quiet village embraced by an ancient forest, young Aiden was known for his boundless curiosity. While other children played in the sunlit meadows, Aiden wandered into the depths of the woods, captivated by whispers of hidden wonders.One day, following a faint trail, Aiden stumbled upon a weathered stone arch draped in vines. Intrigued, he stepped through and found himself in a realm shimmering with ethereal light. Creatures of myth fluttered past, and melodies echoed through the air. Aiden befriended a sprite who spoke in the language of the wind and a gentle giant who shared stories of stars.Yet amid the enchantment, Aiden sensed a looming imbalance. He learned of a fading magic tied to the realm's harmony. With newfound friends by his side, he embarked on a quest to restore balance, weaving together fragments of scattered magic.Through trials and camaraderie, Aiden discovered his inner strength. As he bid farewell to the enchanted realm, he carried with him not just memories, but a profound understanding—that in every forest, and within every heart, lies a tale of courage, friendship, and the enduring magic of discovery.</p></div"
if __name__=='__main__':
    app.run(debug=True)

