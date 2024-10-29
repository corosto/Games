using UnityEngine;

public class ScoreScript : MonoBehaviour {

    private LogicScript logicScript;

    private void Start() {
        logicScript = GameObject.FindGameObjectWithTag("Logic").GetComponent<LogicScript>();
    }

    private void OnTriggerEnter2D(Collider2D collision) {
        if (collision.gameObject.layer == 3) {
            logicScript.addScore(1);
        }
    }
}
