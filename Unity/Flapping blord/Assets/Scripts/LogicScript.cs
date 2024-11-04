using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class LogicScript : MonoBehaviour
{

    private int playerScore = 0;
    public Text scoreText;
    public Text highScoreText;
    public GameObject gameOverScreen;

    private void Start()
    {
        highScoreText.text = "High score: " + PlayerPrefs.GetInt("HighScore").ToString();
    }

    [ContextMenu("Increase Score")]
    public void addScore(int scoreToAdd)
    {
        AudioManagerScript.AudioManagerInstance.PlaySFX("Point");
        playerScore += scoreToAdd;
        scoreText.text = playerScore.ToString();
    }

    public void restartGame()
    {
        SceneManager.LoadScene(SceneManager.GetActiveScene().name);
    }

    public void gameOver()
    {
        gameOverScreen.SetActive(true);

        int highScore = PlayerPrefs.GetInt("HighScore");

        if (highScore < playerScore)
        {
            PlayerPrefs.SetInt("HighScore", playerScore);
        }
    }
}
