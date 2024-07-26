import { UserInfo } from "../types/UserInfo";
import { Question } from "../types/Question";

export const UpdateUserQuestions = (userInfo: UserInfo, question: Question) => {
  console.log("User Info:", userInfo);
  console.log("Question:", question);
};
