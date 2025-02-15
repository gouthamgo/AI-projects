import { HfInference } from '@huggingface/inference';
import 'dotenv/config';  


const hf = new HfInference(process.env.HUGGINGFACEHUB_API_TOKEN);

const inputText = "The definition of machine learning inference is ";

(async () => {
    const response = await hf.textGeneration({
        inputs: inputText,
        model: "mistralai/Mixtral-8x7B-Instruct-v0.1"
    });

    console.log(response);
})();



