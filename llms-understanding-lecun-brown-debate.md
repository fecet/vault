# Do LLMs Understand? AI Pioneer Yann LeCun Spars with DeepMind’s Adam Brown.

Speaker 1:
It's a pleasure to have Adam, my colleague and friend, and Yann, who's been with us before. Yann, you really are all over the news right now. I've gotten so many people forwarding articles about you. This week, it all kicked off on Wednesday.

Do you want to discuss the... I can just say the headline. The headline was the equivalent of Yann LeCun, chief scientist, leaves meta. Do you care to comment?

Speaker 3:
I can neither confirm nor deny.

Speaker 1:
Okay. So all of the press, the core that's here to get the scoop cannot get the scoop tonight. All right, well,  you can come afterwards and buy Yann a drink and see how far you get with The Frenchman had some wine upstairs.

So we have this era where every time any of us turn on the news,  look at the computer,

 read the paper, we're confronted with conversations ...about the societal implications of AI and whether it's about economic upheaval or the potential for political manipulation or AI psychosis.

There's a lot of pundits out there discussing this and it is a very important issue.

I kind of want to push that towards the end of our conversation because what a lot of people who are discussing this don't have is the technical expertise that's on this stage. And so I really want to begin by grounding this.

In that technical scientific conversation. And so I want to begin with you, Yann, about neural nets. Here's this instance of kind of biomimicry, where you have these computational neural networks that are emulating human networks.

Can you describe to us what that means that a machine is emulating human neural networks?

Speaker 3:
Well, it's not really mimicry, it's more inspiration, the same way, I don't know, airplanes are inspired by birds, right?

Speaker 1:
That didn't work, I thought.

Speaker 3:
Say again?

Speaker 1:
But I thought that didn't work, copying birds with airplanes.

Speaker 3:
Well, in the sense that, you know, airplanes have wings like birds,  and they Neural networks generate lift by propelling themselves through the air. But then the analogy stops there.

And the wing of an airplane is much simpler than the wing of a bird. But yet the underlying principle is the same. So neural networks are a bit like that, like our two real brains, as airplanes are to birds.

They're much simplified in many ways. But perhaps some of the underlying The same we don't actually know because we don't really know the sort of underlying algorithm of the cortex,

 if you want, or the method by which the brain organizes itself and learns. So we invented substitutes, sort of like, you know, birds flap their wings and not airplanes, right? They have propellers or turbojets.

You know, in neural nets, we have learning algorithms, and they allow artificial neural nets to learn. In a way that we think is similar to how the brains learn. So the brain is a network of neurons.

The neurons are interconnected with each other. And the way the brain learns is by modifying the efficacy of the connections between the neurons.

And the way a neural net is trained is by modifying the efficacy of the connections between those simulated neurons. Each of those is like a We call it a parameter. You see this is a price, the number of parameters of a neural net, right?

So the biggest neural net at the moment have You know, hundreds of billions of parameters,  if not more, and those are the individual coefficients that are modified by training.

Speaker 1:
And how has deep learning emerged in this discussion? Because deep learning came along the path after thinking about neural nets,  and this has been since the 80s or earlier even.

Speaker 3:
Yeah, 80s roughly. So early neural nets. The first ones are capable of learning or learning something useful at least in the 50s. We're shallow. You could basically train a single layer of neurons, right? So you would feed the input.

And train the system to produce a particular output,  and you could use those things to kind of recognize or classify relatively simple patterns,  but not really sort of complex things. And people at the time, even in the 60s,

 realized that the way to make progress was going to be able to train neural nets with multiple layers. They built neural nets with multiple layers, but they couldn't train all the layers. It would only train the last layer, for example.

And They didn't really find, until the 1980s,  nobody found really a good way to train those multilayer systems,  mostly because the neurons that they had at the time were the wrong type. They had neurons that were binary.

So neurons in the brain are binary. They either fire or they don't fire. And people wanted to reproduce that. So they built simulated neurons that would either be active or inactive.

And it turns out, For the modern learning algorithms to work, we call it backpropagation. You need to have neurons that have sort of graded responses. And that only became practical possible when people realized it could work in the 1980s.

People had the idea before, but they never could really make it work. And so that caused a renewal of interest in neural nets in the 1980s. They had been largely abandoned in the late 60s.

And then they came to the fore again in the mid to late 80s. That's when I started kind of my graduate school basically in 1983.  And there was a wave of interest that lasted about 10 years.

And then interest waned again in the mid 90s until the late 2000 when We rebranded it into deep learning. Neural net had kind of a bad rep. People in computer science and engineering thought neural nets were kind of a bad thing.

It had a bad reputation. And so we branded it into deep learning and sort of brought it back to the fore. And then the results were there in computer vision, in natural language understanding,

 speech recognition to really convince people that this was a good thing.

Speaker 1:
At a very young age, we're interested in theoretical physics, not specifically computer science. And you're watching some of this unfold in some sense from afar. What's the catalyst that sweeps up so many people decades later?

There's this time where it's of great interest,  there's great success in handwriting recognition or visual recognition and these things,  but it's not sweeping up the world.

What happens that brings us to this point where we're all now talking about large language models?

Speaker 2:
So many physicists in the last years have pivoted, shall we say, from working on physics to working on AI. And it really traces back to some of the work that Yann and others did to prove that it works.

Like when it wasn't working, it was just this,  this thing that's over there in computer science and like many things in the world that are not particularly It may be interesting,  but not many physicists are paying attention to it.

But then after, you know, Yann and some of the other pioneers of this field proved that it would work,  it became a totally fascinating subject for physics,  that you link up these neurons together in a certain way.

And suddenly, you get emergent behavior that didn't exist at the individual neuron level.

That seems like a subject that physicists who spend their life imagining how the sort of rich pageantry of the world could emerge from simple laws that immediately attracted the attention of many physicists.

And nowadays, it's a very common career path to do a PhD in physics,  and then apply it to a emergent system. But the emergent system is an emergent network of neurons that collectively give rise to intelligence.

Speaker 1:
Now, let's do a lightning round because you raised the dreaded word intelligence. Everybody in this room very likely has interacted with something that we're now calling an AI. These are all large language models.

And before I ask you to define those for us,  I just want to kind of do a lightning round of what's your yes or no response to certain things. So, Adam, yes or no, are these AIs, these large language models,

 understanding the meaning of the conversations they are having with us? Yes or no?

Speaker 2:
Yes.

Speaker 1:
Yann.

Speaker 3:
Sort of.

Speaker 1:
Perfect.

Speaker 2:
Yann's neurons are not stuck at binary values.

Speaker 1:
Right, exactly. It was my fault for giving you a binary choice. Okay, so that allows me to ask the next question because it's not a foregone conclusion. If you don't say yes to that, it's going to be interesting what you say to this.

Are these AIs conscious?

Speaker 3:
Absolutely not.

Speaker 1:
Adam?

Speaker 2:
Probably not.

Speaker 1:
Will they soon be?

Speaker 2:
I think they'll one day be conscious if progress continues in the way that we're continuing. When is hard to say, but one day.

Speaker 1:
Yann LeCun. Yon.

Speaker 3:
Renaissance.

Speaker 1:
Adam.

Speaker 2:
Most likely Renaissance.

Speaker 1:
I have to throw this out. The same question to the audience, but I'm going to phrase it more colorfully, which I think they'll relate to. Will the robot overlords rise up against humanity? Yes, hands up. Oh, interesting. Okay, no hands up.

Okay, how many robots in the audience? Hands up. Okay.

Unknown Speaker:
So, okay.

Speaker 1:
So that's interesting. See, that's cool. It was a little more nose, maybe, although the light is blinding. All right, we're going to come back and ask that again at the end.

So here we are, these neural nets have been taught to Execute a process we now call deep learning,  and there's other kinds of learning that take off. And what are the large language models specifically,

 which is really what has swept up the news and people's personal experience? We're mostly relating to large language models. And what are the large language models, Adam? Maybe you could take that.

Speaker 2:
Yeah, so large language model is, you've probably played with some of them, ChatGPT,  Gemini made by my company, various others made by other companies.

It is a special kind of neural network that's trained on particular inputs and particular outputs and trained in a particular way. So it is, at heart, it is mainly the kind of deep neural network that was pioneered by Yann and by others,

 but with a particular architecture designed for the following task. It takes text in, so it'll read the first few words of some sentence or the first few paragraphs of some book,

 and it will try and predict what the next word is going to be. And so you take a deep neural network with a particular architecture, and you have it read,  basically, to first approximation, the entire internet.

And for every word that comes along on the entire internet,  all of the text data and now other kind of data you can find,  you then ask it, what do you think the next word's going to be? What do you think the next word's going to be?

And to the extent that it gets it right,  you give it a little bit of reward and strengthen those neural pathways. To the extent that it gets it wrong, you diminish those neural pathways.

And if you do that, it'll just start off spewing just completely random words for its prediction. But if you train it on a million words, it'll still be spewing random words. If you train it on a billion words,

 it'll maybe have just started to learn subject,  verb, object, and various bits of sentence structure. And if you train it as we do today on a trillion words or more,

 tens of trillions of words, then it'll start become the conversation partner that you probably,  I hope, played around with today.

Speaker 1:
Now, it strikes me as intriguing,  like it amuses me sometimes people get Really outraged at their chatbot that they're engaged with when it leads them astray or lies to them. And sometimes I've said, well, it doesn't need to be words.

It might as well be colors or symbols. It's just playing a mathematical game and therefore doesn't have a sense of meaning. Now, I know Adam sort of objected to my summary of that. Do you think that they are extracting meaning?

In the same sense that we do when we are engaging in composing sentences?

Speaker 3:
Well, they're certainly extracting some meaning. But it's it's a lot more superficial than what most humans would extract from from text. Most humans. Intelligence is linked to is grounded into an underlying reality, right?

And language is a way to express phenomena or things in that or concepts grounded in that reality. LLMs don't have any notion of the underlying reality. And so their understanding is is relatively superficial.

They don't really have common sense in the in the way that we understand it. But if you train them long enough, they will Answer correctly most questions that people will think about asking. That's the way they're trained.

You collect all the questions that everybody has ever asked them,  and then you train them to produce the correct answer for this. Now, there's always going to be new questions or new prompts,

 new sequences of words for which the system has not really been trained,  and for which it might produce complete nonsense. So in that sense, they don't have the real understanding of the underlying reality,

 or they do have an understanding, but it's superficial. And so, you know, the next question is how do we fix that?

Speaker 1:
So I could play devil's advocate and say, well,  how do I know that what a human being is doing is that much different? Right? We're trained on lots of language.

We get some dopamine hit or some reward system for having said the right word at the right time and the right grammatical structure for the language that we're immersed in. And we back propagate, we try to do a better job the next time.

In some sense, how is that different than what a human being is doing? And you're saying maybe it's the sensory experience of being immersed in the world?

Speaker 3:
Okay. A typical LLM, as I mentioned, is trained on tens of trillions of words. Typically.

Speaker 1:
It's only a few hundred thousand words. You're just saying sentences. It's combinations.

Speaker 3:
30 trillion words is a typical size for the training set, pre-training of an LLM. A word is represented actually as sequences of tokens, doesn't really matter. And a token is about three bytes. So the total is about 10 to the 14 bytes, right?

One with 14 zeros of training data to train those LLMs. And that corresponds to basically all the text that is publicly available on the internet plus some other stuff.

And it would take any of us something like half a million years For any of us to read through that material,  right, so it's an enormous amount of textual data. Now compare this with what a child perceives during the first few years of life.

Psychologists tell us that a four-year-old has been awake a total of 16,000 hours. And there's about One byte per second going through the optic nerve, every single fiber of the optic nerve. We have two millions of them.

So it's about two megabytes per second getting to the visual cortex. During 16,000 hours, do the arithmetic since it's about 10 to the 14 bytes.

A four-year-old has seen as much visual data as the biggest LLM trained on the entire text ever produced. And so what that tells you is that there is way more information in the real world,  but it's also much more It's complicated.

It's noisy. It's high dimensional. It's continuous. And basically the methods that are employed to train LLMs do not work in the real world.

That explains why we have LLMs that can pass the bar exam or solve equations or compute integrals like college students and solve math problems. But we still don't have a domestic robot that can You know, do the chores in the house.

We don't even have level 5 self-driving cars. I mean, we have them, but we cheat. So, I mean, we certainly don't have self-driving cars that can learn to drive in 20 hours of practice like any teenager,  right?

So, obviously, we're missing something very big to get machines to the level of human or even animal intelligence, right? Let's not talk about language. Let's talk about how a cat is intelligent. or a dog.

We're not even at that level with AI systems.

Speaker 1:
Adam, you impart more comprehension on the part of the LLMs at this point already.

Speaker 2:
I think that's right. So I mean, Jan ...is making excellent points that the LLMs are much less, for example, sample efficient than humans. Humans, or indeed, your cat, or just a cat, I don't know if it was your cat or a cat...

Speaker 1:
He's a very smart cat.

Speaker 2:
...in your example, is able to learn from many fewer examples than a large language model,  for example, can learn from, that takes way more data to teach it to the same level of proficiency. And that's true.

And that is the thing that is better about the architecture of animal minds compared to these artificial minds that we're building. On the other hand, sample efficiency isn't everything.

We see this frequently, in fact, when we try and You know, before large language models,  when we try and put machines on, you know, make artificial minds to do other tasks,

 even the famous chess bots that we built on, built on top of large language models,  the way they were trained, sort of AlphaZero and various other ones, they would play each other,  they would play itself at chess a huge number of times.

And to begin with, it would just be making random moves. And then every time it won or lost the game,  when it was playing itself, it was sort of you know,  reward that neural pathway or punish that neural pathway.

And they play each other at chess again and again. And when they played as many games as a human grandmaster has played, they were still making essentially random moves.

But they were not confined to playing the same number of games that a human grandmaster could play. Because silicon chips are so fast, because we can build them with such parallel processing,

 they were able to play many more games than any human could ever play in their lifetime. And what we found is that when they did that,  they reached and then far surpassed the level of human chess players.

They're less sample efficient, but that doesn't mean they're worse at chess. It's clear that they're much better at chess. So too with understanding. We, it is true that we can, you know, it is harder with these things to,

 you need more samples to get them up to the same level of proficiency. But the question is, once they've reached that,  can we use the fact that they are so much more general,

 and so much more, so much faster and more inerrant to push beyond that? I mean, another example, perhaps with the cat, is a cat is in fact,  even more sample efficient than a human. A human takes a A year to learn to walk.

A cat learns to walk in a week or so. It's much faster. That does not mean that a cat is smarter than a human. It does not mean that a cat is smarter than a large language model.

The final question at the end should be what is the capabilities of these things? How far can we push the capabilities? And on Almost every, except for the somewhat impoverished metric of sample efficiency on every metric that counts,

 we've pushed these large language models far beyond the frontier of cat intelligence.

Speaker 1:
Yes, I don't understand why we're not making cats. Sorry, what was that Yann?

Speaker 3:
I mean, certainly the LLMs in question have much more accumulated knowledge than cats or even humans for that matter. And we do have many examples of computers being far superior to humans in a number of,

 you know, different tasks like playing chess, for example. That's humbling. I mean, it just means that humans just suck at chess. That's all it means. No, we really suck at chess and Go, by the way, even more.

And many other tasks at computers are much better than us. At solving. So certainly LLMs can accumulate a huge amount of knowledge. And some form of them can be trained to translate languages, understand spoken language,

 and translate it into another one from, you know, 1000 languages to another 1000 languages in any direction. No human can do this. So they do have superhuman capabilities. But the ability to Learn quickly,

 efficiently to apprehend a new problem that we've never been trained to solve and be able to come up with a solution. And to really, you know, understand a lot about how the how the world behaves.

That is still out of reach of AI systems at the moment.

Speaker 2:
I would I mean,  we've had recent successes with this where it is not the case that they're just taking problems that they've seen before,  letter for letter. And looking up the answer in a lookup table,

 or even that they are in some sense doing pattern matching,  but they're doing pattern matching at a sufficiently elevated level of abstraction,  that they're able to do things that they've never seen before,  and no human can do.

So there's a competition each year called the International Math Olympiad. It is the very smartest I finish in high school, maths, teenagers in the entire world. They're all given six problems each year, the pinnacle of human intelligence.

I have some mathematical ability, I look at these problems, I don't even know where to start. This year, we fed them into our machine. As did a number of other LLM companies.

And they took these problems they'd never seen before, they were completely fresh, didn't appear anywhere in the training data,  completely made up, took a whole bunch of different ideas, combined the different ideas,

 and got a score on these tests that was better than all except the first dozen,  the top dozen humans on the planet. I think that's, that's pretty impressive intelligence.

Speaker 1:
I guess the question is back to this idea, do they understand? We can look at the mathematics of the model. There's some input data. We understand what it's doing. It is a black box, which is kind of fascinating.

It's just so complex that it's not as though we can't do that with the human mind either. It's not as though you can look at the inner workings and see exactly what they're doing. To some extent, it is a black box,

 but we presume it's just Doing these calculations,  it's moving these matrices, it's working in some vector space, it's doing some higher dimensional thing. I have some experience of understanding. I guess people are still grasping at that.

Is it having some experience of understanding? Is it important whether or not they experience understanding? Is that sufficient to call it comprehension of meaning?

Speaker 2:
Are you describing understanding as a behavioral trait here,  where it gives the right answers to problems,  or whether it deeply at the neural level understands?

Speaker 1:
Yeah, I'm, I'm completely at the whims of the philosophers here. No, I, I don't know if I understand that at my, at the human level,  right, I can't tell you what process I'm executing at At the moment either,  right?

But I'd have some intuitive subjective experience that I understand the conversation. Obviously not that well. But when I'm talking to you, I feel you are understanding. And when I'm talking to ChatGPT, I do not.

And you're telling me I'm mistaken. It's understanding as well as I am, or you are.

Speaker 2:
In my opinion, it is understanding. Yes. And I think there's two different pieces of evidence for that. One is, I think if you talk to them, like,  if you talk to them and ask them about difficult concepts,

 I'm frequently surprised and with every passing month and every new model that comes out,  I am more and more surprised at the level of sophistication with which they're able to And so just at that level,  it's super impressive.

I would really encourage everybody here to talk to these large language models. If you've not already, you know, when the science fiction writers imagined that we built some sort of Turing test passing machine that was going to,

 you know, some new alien intelligence that we'd have in a box,  they all imagined that we'd sort of ...hide it in a basement,  you know, in a castle surrounded by a moat with arms guards,

 and we'd only have like a priestly class who could be able to go and talk to it. That is not the way it worked out. The way it's worked out is the first thing we did is we immediately hooked it up to the internet.

And now anybody can go talk to it. And I would highly encourage you to talk to these things and explore in areas that you know. To see both their limitations but also their strength and their depth of understanding.

So I'd say that's the first piece of evidence. The second piece of evidence is you said they're a black box. They're not exactly a black box. We do have access to their neurons.

In fact, we have much better access to the neurons of these things than we do with a human. It's very hard to get IRB approval to slice open a human while they're doing a math test and see how their neurons are firing.

And if you do do that, you can only do that once on a per-human basis. Whereas these neural networks, we can freeze them, replay them, write down everything that happened.

If we're curious, we can go and prod their neurons in certain ways and see what happened. And so this is, it's still rudimentary, but this is the field of interpretability,

 mechanistic interpretability, trying to understand not just what they say, but why they say it,  how they think it. And when you do that, we see When you feed them a math problem,

 there's a little bit of a circuit there that computes the answer. We didn't program it to have that. It learned how to do that. While trying to predict the next token on all of this text,

 it learned that in order to most accurately predict the next word,  it needed to figure out how to do maths,  and it needed to build a sort of proto-little circuit inside it to do the mathematical computations.

Speaker 1:
Now, Yann, you famously threw a slide up at one of your keynote lectures that was very provocative, very scholarly. It said, machine learning sucks, I believe. And then that kind of went wild. Yann LeCun says machine learning sucks.

Why are you saying machine learning sucks? Adam has just told us how phenomenal it is. He talks to them and wants us to do the same. Why do you think it sucks? What's the problem?

Speaker 3:
Well, that statement has been widely misinterpreted, but the point I was making is the point that we both made,  which is that why is it that a teenager can learn to drive a car in 20 hours of practice,

 a 10-year-old can clean up the dinner table and fill up the dishwasher the first time you ask the child to do it,  whether the 10-year-old would want to do it is a different story. You know, certainly can.

We don't have robots that are anywhere near this. And we don't have robots that are even anywhere near the You know,  physical understanding of reality of a cat or a dog. And so in that sense, machine learning sucks.

It doesn't mean that the deep learning method, the backpropagation algorithm, the neural nets suck.

Speaker 1:
That was obviously excellent. Yes.

Speaker 3:
Obviously, that's great.

Speaker 1:
Yeah.

Speaker 3:
And we don't have any alternative to this. And I certainly believe that You know, neural nets and deep learning and back propagation would be,  you know, are with us for a long time,  would be the basis of future AI systems.

But how is it that, you know, young humans can learn how the world works in the first few months of life? It takes nine months for human babies to learn intuitive physics like gravity, inertia, and things like this.

Baby animals learn this much faster. They have smaller brains, so it's easier for them to learn. They don't run to the same level, but they do learn faster. And so, you know, it's this type of learning that we need to reproduce.

And we'll do this with backprop with neural net with deep learning. It's just that we're missing A concept, an architecture. So I've been making proposals for the type of architectures that could possibly run this kind of stuff.

You know, why is it that LLMs handle language so easily? It's because as Adam described, you train an LLM to predict the next word. Or the next token, doesn't matter. There's only a finite number of words in the dictionary.

So you can never actually predict exactly which word comes after a sequence,

 but you can train a system to produce essentially what amounts to a score for every possible words in your dictionary or a probability distribution over every possible words.

So essentially what LLM does is that it produces a long list of numbers between 0 and 1 that sum to 1,  which for each word in the dictionary says,  this is the likelihood that this word appears right now.

You can represent the uncertainty in the prediction this way. Now, try to translate it. The same principle, instead of training a system to predict the next word,  feed it with a video and ask it to predict what happened next in the video.

And this doesn't work. I've been trying to do this for 20 years. And it really doesn't work if you try to predict at the pixel level. And it's because the real world is messy.

There's a lot of things that may happen, plausible things that may happen. And you can't really represent a distribution of all possible things that may happen in the future,  because it's basically an infinite list of possibilities.

And we don't know how to represent this efficiently. And so those those techniques that work really well for text or for sequences of symbols do not work for real world sensory data. They just don't. They absolutely don't.

And so we need to invent new techniques. So one of the things I've been proposing is one in which the system learns an abstract representation of what it observes and it makes prediction in that abstract representation space.

And this is really the way humans and animals function. We find abstractions that allow us to Make predictions while ignoring all the details we cannot predict.

Speaker 1:
So you really think that despite the phenomenal successes of these LLMs that they are limited and their limit is quickly approaching,

 you don't think that they're scalable to this You know, artificial general intelligence or a super intelligence.

Speaker 3:
That's right. No, they don't. And in fact, we see the performance saturating. So we see progress in some domains like mathematics, for example. And mathematics and code generation, you know, programming,

 are two domains where the manipulation of symbols actually gives you something,  right? As a physicist, you know this, right? You write the equation, and it actually kind of You can follow it and it drives your thinking to some extent,

 right? I mean, you drive it by intuition, but the symbol manipulation itself actually has meaning. So this type of problems, LLMs actually can handle pretty well,

 where the reasoning really consists in kind of searching through sequences of symbols. But it's only, there's only a small number of problems for which that's the case. Chess playing is another one.

You search through sequences of moves that, you know, for a good one,  Or sequences of derivations in mathematics that will produce a particular result,  right?

But in the real world, you know, in high dimensional continuous things where the search has to do with,  like, how do I move my muscles to, you know, grab this, you know,

 grab this, this, this glass here, I'm not going to do it with my left hand,  right? I'm going to have to Change hand with this and then grab it, right? You need to plan and have some understanding of what's possible, what's not possible,

 that, you know, I can't just attract the glass, you know, by telekinesis,  or I can't just make it appear in my left hand like this. I can't have my hand kind of cross my body.

Like, you know, all of those intuitive things, we learned them when we were babies. And we learn, you know, how our body reacts to our controls and how,  you know, the The world reacts to the actions we take.

So, you know, if I push this glass, I know it's going to slide. If I push it from the top, maybe it's going to flip. Maybe not, because the friction is not that high. If I push with the same force on this table, it's not going to flip.

You know, we have all those intuitions that allow us to kind of apprehend the real world. But this is, it turns out, much, much more complicated than manipulating language.

We think of language as kind of the epitome of You know, human intelligence and stuff like that. It's actually not true. Language is actually easy.

Speaker 1:
Is it the Moravec paradox that what computers are good at, humans are bad at? What humans are good at, computers are bad at?

Speaker 3:
We keep running into the Moravec paradox.

Speaker 1:
Now, Adam,  I know that you are less pessimistic about the potential of the current Neural net deep learning paradigm and you see the potential for a great escalation in success and you don't see it saturating.

What's your thought about that?

Speaker 2:
I don't. That's right. And so yeah, we have witnessed over the last five years,  the most extraordinary run up in capabilities in any system I've ever seen. This is what transfixed my attention.

It's what transfixed many other people in AI and neighboring fields to focus all of our attention on this matter. I don't see any slowdown in the capabilities. A year ago,

 if you just look at all of the all of the metrics we use to judge how good these large language models are,  they're getting stronger and stronger and stronger. Things that they, you know, the model from a year ago, today would be,

 you know, table stakes would be considered extremely poor. Every few months, these things push the capabilities. And if, if you track their capabilities on all of these tasks,  they're heading towards superhuman on almost all of them.

It's already better gives better legal advice than than a lawyer. It gives better It's a better poet than almost every poet you will come.

In my little area of physics, I use it because like there's something I kind of should know but I don't. I'll ask the language model and it will not only tell me what the right answer is,

 it will patiently and I should say non-judgmentally listen while I explain my misconception to it and it will carefully debunk my misconception.

The extraordinary run-up in capabilities that we've seen over the last five years and that continues up to the present is extremely tantalizing to me and many other people in San Francisco.

And maybe Yann is correct that we're just going to suddenly saturate and all of these straight lines that have been going up steadily for the last five years are suddenly going to stop going up.

But I am mighty curious to see whether we can push it further. And I've actually seen no indication whatsoever that it's slowing down. Every indication I've seen is that these are improving. And we don't know how far to go,

 because once it's a better coder than almost all our best coders,  it can start improving itself. And then we're really in for a wild ride.

Speaker 3:
Well, we've had better coders than the original coders of 1950s, you know, for six decades or so,  that's called compilers. I mean, we, we keep getting confused.

About the fact that it's not because machines are good at a certain number of tasks that they have all the underlying intelligence that we assume a human having those capabilities will have,  right?

We're fooled into thinking those machines are intelligent because they can manipulate language. And we're used to the fact that people who can manipulate language very well are Implicitly smart,  but we're being fooled. Now, they're useful.

There's no question. You know, we can use them to do what you said. I use it for similar things. Great. They're great tools, like, you know, computers have been for the last five decades. But let me make an interesting historical point.

And this is maybe due to my age. There's been generation after generation of AI scientists since the 1950s,  claiming that the technique that they just discovered What's going to be the ticket for human level intelligence?

You see declarations of Marvin Minsky, Newell and Simon, you know, Frank Rosenblatt, who invented the Perceptron,  the first learning machine in 1950, saying like, within 10 years,  we'll have machines that are as smart as humans.

They were all wrong. This generation with LLM is also wrong. I've seen three of those generations in my lifetime. Okay. So, you know, it's just another example of being fooled.

And in the 50s, Noah and Simon, pioneers of AI, came up with a program. They said, well, you know, really what humans are doing is in reasoning. It's really a search, right? Every reasoning can be reduced to a kind of search.

So you formulate a problem, you write a program that tells you whether a particular proposal for a solution is a solution to your problem,  and then you just have to search for all possible combinations,

 all possible hypotheses for one that actually matches,  satisfies the constraint. That's it. We're going to write a program that does this, and we're going to call it the General Problem Solver, GPS. 1957, I think.

They won the Turing Award for things like that, and it was great. But then they didn't realize that all the interesting problems actually have a complexity that grows exponentially with the size of the problem.

So in fact, you can't really use this technique to build intelligent machines. It can be a component of it, but it's really not the thing. Simultaneously, Frank Rosenblatt came up with a perceptron, a machine that could learn.

And he said, if we can train a machine, then it can become infinitely smart. And so within 10 years, we'll have, we just need to build bigger perceptrons, right? Not realizing that you need to train multiple layers,

 and that turned out to be difficult to find a solution for this. Then in the 1980s, there was expert systems. Reasoning is fine.

Just write a bunch of facts and a bunch of rules and then just deduce all the facts from the original facts and the rules. Now we can reduce all the human knowledge into this. The coolest job is going to be knowledge engineer.

You're going to sit down next to an expert and then write down all the rules and the facts and turn this into an expert system. And, you know, everybody was excited about this. And there were, you know, billions that were invested.

Japan started the fifth generation computer program project, which was going to revolutionize computer science. Complete failure. Okay, it created an industry, it was useful for a few things.

But basically, the cost of reducing human knowledge to rules was just too high for most problems. And so the whole thing collapsed. Then there was neural nets, the first, the second wave of neural nets, 1980s,

 you know, which we now call deep learning, a lot of interest. But then it was before the internet, we didn't have enough data, we didn't have powerful computers.

And now we're going through the same cycle again, and we're getting fooled again.

Speaker 1:
So just to be, oh, Adam, please.

Speaker 2:
In technologies, every dawn has before it false dawns. That doesn't mean we'll never hit the dawn. I guess I would like, Yann, if you think that LLMs are going to saturate,  what is a concrete task that they will never be able to do?

That an LLM augmented by the tools we give it today will never be able to perform?

Speaker 3:
Clear out the dinner table, fill up the dishwasher.

Speaker 2:
Okay.

Speaker 3:
And that's easy compared to...

Speaker 2:
I'm skeptical.

Speaker 3:
That's super easy compared to fixing your toilets. Okay, a plumber, right? You're never going to have a plumber with LLMs. You're never going to have a robot driven by LLMs. It just cannot understand the real world. It just can't.

Speaker 1:
So I want to clarify for the audience that you're not saying that machines or robots won't be able to do this. That's not your position. You think they will.

Speaker 3:
They will. They absolutely will.

Speaker 1:
But just not by this algorithmic approach or this particular approach of the deep learning on the neural nets.

Speaker 3:
If the programmer working on succeeds, which may take a while.

Speaker 1:
This is cheaper.

Speaker 3:
And you know, all the things, world models and things that go with it. If it succeeds, which may take, you know, several years, then we may have, you know, AI systems. There's no question that at some point in the future,

 we will have machines that are smarter than humans in all domains that,  you know, where humans have abilities. There's no question about that. It will happen. Okay.

It'll probably take longer than, you know, some of the people in Silicon Valley at the moment are seeing it. It will. And it will not be LLMs. It will not be generative models that predict discrete tokens.

It will be models that learn abstract representations and make predictions on abstract representations and can reason about what is going to be the effect of me taking this action.

Can I plan a sequence of actions to arrive at a particular goal?

Speaker 1:
You call this self-supervised learning?

Speaker 3:
No, so self-supervised learning is used also by LLMs.

Self-supervised learning is the idea that you train a system not for a particular task other than capturing the The underlying structure of the data you show it and one way to do this is to give it a piece of data.

We corrupt it in some way by removing a piece of it, for example,  masking a piece of it, and then training a bit neural net to predict the piece that is missing. So LLMs do this, right? You take a text, you remove the last word,

 and you train the LLM to predict the word that is missing. You have other types of language models that actually fill up multiple words. They turn out to not work as well as the ones that just predict the last one.

At least for certain tasks. You can do this with video. If you try to predict at the pixel level, it doesn't work or it doesn't work very well.

My colleagues at Meta probably boiled a couple of small lakes in the West Coast trying to make this work to cool the GPUs. It simply doesn't work. So you have to, you know, come up with those new architectures like JIPA and stuff like that.

And those kind of work like we have models that actually understand video.

Speaker 1:
And, Adam, are people exploring other ways of building an architecture or imagining a computer mind,  the actual fundamental structure of a computer mind and how it would, how it would learn,  how it would acquire information?

One of the criticisms, as I understand it,  is it's a lot of the LLMs are trained for this one specific task of This discrete prediction of these tokens,

 but something that is more unpredictable, like how the audience is distributed in this room,  what might happen with the weather next? Unpredictable, more human experience based phenomenon.

Speaker 2:
Certainly, all kinds of explorations are being made in all kinds of directions, including Yann's, and a thousand flowers bloom.

But all of the resources, I mean, the bulk of the resources right now are going into large language models and large language model-like applications,  including taking in text.

To say that they are, it's a specialized task predicting the next token,  I think that's a Not a helpful way to think about it. It is true that the thing that you train them on is given this corpus of text,

 I mean, there are other things we do as well,  but the bulk of the compute goes to given this corpus of text,  please predict the next word, please predict the next word, please predict the next word.

But we have discovered something truly extraordinary by doing it,  which is that given a large enough body of text to be able to reliably predict the next word or,

 you know, To do it well enough to predict the next word, you really need to understand the universe. And we have seen the emergence of understanding of the universe as we've done that. So I would liken it a little bit.

I mean, in physics, we're very used to systems where you just take a very simple rule,  And, you know, by the repeated application of that very simple rule, you get extremely impressive behavior. We see the same with these LLMs.

And another example of that will maybe be evolution. You know, at each stage in evolution, you just say, biological evolution, you just say,

 you know, maximize the number of offspring, maximize the number of offspring, maximize the number of offspring,  a very sort of unsophisticated learning objective. But out of this simple learning objective, repeated Many, many times,

 you eventually get all of the splendor of biology that we see around us and indeed this room. So the evidence is that predicting the next token, while a very simple task,

 because it's so simple, we can do it at massive scale, huge amounts of compute. And once you do it at huge amounts of compute, you get an emergent complexity.

Speaker 1:
So I guess the next question could be related to evolution. However, this intelligence emerges that you both imagine is certainly possible. You don't think there's anything special about this wetware, that there will be machines,

 we just have to figure out how to launch them, that will have capacities that we align as a kind of Intelligence or maybe consciousness? That's almost a different question. Will consciousness be a crutch machines don't need? I don't know.

We can talk about that. But is there a point in the evolution of these machines where they're going to say,  oh, how quaint, mom and dad. You made me in your image with these human neural nets.

But I know a way, a much better way, having scanned 10,000 years of human output to make machine intelligence. And I'm going to evolve. And leave us in the dust.

I mean, yeah, why are we imagining they would be limited at that capacity to the way we design them?

Speaker 2:
Absolutely. This is this idea of recursive self-improvement, where When they're bad, they're useless. But when they get good enough, and strong enough,  you can start using them to augment human intelligence,

 and perhaps, eventually just be fully autonomous, and replace and make future versions of them. Once we do that, I mean, I think what we should do is just take this large language model paradigm that's currently working so well,

 and just see how far we can push it, you know,  it keeps every time someone says there's a barrier,  it pushes through the barrier over the last five years.

But eventually, These things will get smart enough, and then they can read Yann's papers,  read all the other papers that have been made,  try and figure out new ideas that none of us have thought of.

Speaker 3:
So I completely disagree with this. So LLMs are not controllable. It's not dangerous because they're not that smart, as I explained previously. And they're certainly not autonomous in a way that we understand autonomy.

We have to distinguish between autonomy and intelligence. You can be very intelligent without being autonomous. And you can be autonomous without being intelligent. You can be dangerous without being particularly intelligent.

And you can want to be dominant without being intelligent. In fact, that's going to be inversely correlated in the human species. You know, politics. I won't cite names.

So, I think what is required is systems that are intelligent, in other words,  can solve problems for us, but it will solve the problem we give them. Okay. And again, that would require a new design than LLMs.

LLMs are not designed to fulfill a goal. They're designed to predict the next work. And we fine tune them so that they behave, you know, for particular questions, they answer in a particular way.

But there's always what's called a generalization gap, which means you can never train them for every possible question. And there's a very long tail. And so they're not controllable.

And again, that doesn't mean they're very, it's very dangerous, because they're not that smart. Now, if we build systems that are smart, we want them to be controllable. And we want them to be driven by objectives, we give them an objective.

And the only thing they can do is fulfill this objective, according to their,  you know, internal model of the world, if you want. So plan a sequence of actions that will fulfill that objective.

If we design them this way, And we also put guardrails in them so that in the process of fulfilling the objective,  they don't do anything bad for humans. So the usual joke is, if you have a robot,

 Domestic robot and you ask it to fetch you coffee and someone else is,  you know, someone is standing in front of the coffee machine. You don't want your robot to just, you know, kill that person to get access to the coffee machine, right?

So we want to put some guardrails into the behavior of that robot. And we do have those guardrails in our head. Evolution built them into us, right? So we don't kill each other all the time.

I mean, we do kill each other all the time, but not, you know,  not all the time, all the time. I mean, you know, we feel empathy and things like that. And that's just built into us by evolution.

That's the way evolution sort of hardwire guardrails into us. So we should build our AI systems the same way, have objectives and goals,  drives, but also You know, God rails inhibition, basically.

And, and then they will solve problems for us, they will amplify our intelligence,  they will do what we ask them to do. And our relationship to those intelligence system will be like the relationship of, let's say,

 a professor with graduate students who are smarter than them, right? I mean, I don't know about you, but I have students who are smarter than me. It's the best thing that can happen to you, right? It is.

Speaker 1:
It's the best thing that can happen.

Speaker 3:
Right. So we'll be working around with AI assistants. They will help us in our daily lives. They'll be smarter than us, but they will work for us. They'll be like our staff. Again, there is a political analogy here, right?

A politician, right, is a figurehead, and they have a staff of people, all of whom are smarter than them,  right? So it's going to be the same thing with the AI system,  which is why to the question of renaissance,  I said renaissance.

Speaker 1:
So you have no concerns about the safety of the current But the question is, maybe we should stop there. I mean,

 why is it necessary for us to scale up so widely that every single person has this super intelligence in their pocket on their iPhone? Is that really necessary?

A friend of mine was saying, it's like bringing a ballistic missile to a knife fight. I mean, is this necessary that every person has a ballistic missile capability? Or should we stop here where we have these controllable systems?

Speaker 3:
We do the same thing about teaching people to read,  giving them a textbook of chemistry of volatile chemicals,  you know, with which you can make explosives, or nuclear physics book, right?

I mean, we do not question the idea that Knowledge and more intelligence is good, intrinsically good, right? We do not question anymore the fact that the invention of printing press was a good thing, right? It made everybody smarter.

It gave access to knowledge to everyone, which was not possible before. It incited people to learn to read. It caused the Enlightenment. It also caused 200 years of, you know, religious wars in Europe. Okay, but we got over it.

Speaker 1:
Yeah.

Speaker 3:
But it caused the Enlightenment, because, you know, the emergence of philosophy, science, democracy,  the American Revolution, the French Revolution, all of that would not have been possible without the printing press.

So, you know, every Technology that, particularly communication technology, but technology that amplifies human intelligence, I think is intrinsically good.

Speaker 1:
Now, Adam, people are concerned. I'm sure they'll feel very reassured that Yann is not concerned when these doomsday scenarios you think are highly exaggerated.

But are you concerned about some of the safety issues around AI or our ability to really keep the relationship balanced in the direction that we want it to be?

Speaker 2:
I think to the extent that I think this is going to be a more powerful technology than Yann thinks it does,  I am more concerned. I think it's going to be a very powerful,  to the extent that it is a very powerful technology,

 it'll have both positive and negative impacts. And I think it's very important to make sure that we work together to make sure that the positive impacts are outweigh the negative impacts. I think that path is totally open to us.

There are a huge number of possible positive impacts and we could talk about some of those perhaps. But we need to make sure that that happens.

Speaker 1:
Now let's talk about agentic misalignment, which is the phrase that's been passed along. It was my understanding there was reports recently that when Claude IV was rolled out,  that those in simulations and tests One of the models was,

 or I don't know if there's a singular model,  I don't know if it thinks of itself as a singular entity or they,  but the model exhibited resistance to rumors in the simulation that it was going to be replaced.

It was Sending messages to its future self, trying to undermine the intentions of the developers. It faked legal documents and it threatened to blackmail one of the engineers, right? So this notion, they were concerned.

So this notion of agentic misalignment, is that something that you're concerned with, that there will be a power over,  say, financial systems, heating and cooling systems, the energy grid?

And that they will resist its developers intentions.

Speaker 2:
Yeah, so that paper was a paper by Anthropic, which is a company in San Francisco,  not my company, but a company that takes safety very seriously. And they did a slightly mean thing to their LLM, where they gave it a scenario,

 sort of philosophy professor style scenario, where it had to do a bad thing to stop an even worse thing happening. Sort of, you know, Utilitarian ethics and deontological ethics colliding,

 and it was eventually persuaded by them to do the utilitarian thing. And that's kind of not what we want, I would say. We want it that if it has a rule that it will not lie,  that it will not lie, no matter what.

And to their credit, they tested it for that,  found that it would occasionally act deceptively if promised that by doing so it could save that many lives. These are tricky things that human philosophers wrestle with.

I think we need to be careful to train them to obey our command. And we spend a lot of time doing that.

Speaker 1:
Who's us? Isn't this a big concern? We're assuming that all of humanity is aligned in our intentions. That's clearly not the case. And I know, Yann, you, in a very interesting way, argue for open source,

 which some people would say is even more dangerous because now anyone can have access to it. It's dangerous enough that it's in the hands of a small number of people who Rule corporations,

 but let alone everyone having it, maybe that is dangerous. But again, who's us and we?

Speaker 3:
The danger is, if we don't have open source AI systems, okay, in the future,  every single one of our interaction with the digital world will be mediated by an AI system. Right? We're not going to go to a website or search engine or whatever.

We're just going to talk to our AI system, however it's built. So, our entire information diet will come from AI systems. Now, what does it mean to culture, language, democracy, everything,

 if those systems come from a handful of companies on the West Coast of the US or China? I tell you, no country in the world outside the US and China likes the idea.

So we need a high diversity of AI assistant for the same reason we need a high diversity of the press. We cannot afford to have just a handful of proprietary system coming out of a small number of companies.

There is one thing I'm scared of, and that's it, okay? If we don't have open platforms, we're going to have, you know,  capture of information flow by a handful of companies,  some of which we may not like.

Speaker 1:
And so... So how can we be certain that these, when they really are self-motivated agents,  if that ever actually happens, that they won't collude, fight amongst themselves, want to wrestle for power,

 that we won't be sitting back watching conflicts that we simply couldn't have imagined before?

Speaker 3:
We give them clear objectives, and we build them in such a way that the only thing they can do is fulfill those objectives. Now, this is not It doesn't mean it's going to be perfect,  but the question of AI safety in the future,

 I'm worried about it in the same way that I'm worried about the question of reliability of turbojets,  okay? I mean, turbojets, I mean, it's amazing. I don't know about you, but, and my dad was an aeronautical engineer,

 but I'm totally amazed by the fact that you can fly halfway around the world in complete safety on a two-engine airplane. It's amazing, right? And we feel completely safe doing this.

It's a magical production of, you know, engineering of the modern science and engineering of the modern world. AI safety is a problem of this type. It's an engineering problem. I think the fears are caused by people who think about You know,

 science fiction scenario where somewhere someone invents the secret to superintelligence,  turns on the machine and the next second it takes over the world. That is complete BS. Like, the world doesn't work this way.

Certainly the world of technology and science doesn't work this way. The emergence of superintelligence is not going to be an event. As we see, we have superintelligent systems that can do superintelligent tasks, you know,

 and there is kind of continuous progress one at a time. But, you know, we're going to find some, you know,  better recipe to build AI systems that may have kind of a more general intelligence than we currently have.

And we'll have systems, there's no question, that are smarter than humans. But we'll build them so that they fulfill the goals we give them, subject to guardrails.

Speaker 1:
I was going to again question this idea of we know that if we can code them in a certain way,  somebody could recode them and the concept of bad actors. But before we fall into that hole, I have a plant in the audience.

Does my plant have a mic? Does my plant know who he is? Does my, Meredith, Isaac, does my plant have a mic? Yes? Oh, but he doesn't have the mic. Okay, David, can you shout? Okay, so I want to introduce the philosopher of mine, David Chalmers.

I'm going to give you a very brief introduction. David, I can't see you, but I said that you could be my plant to ask a question. Do you want to throw something down here?

Unknown Speaker:
Okay, Janna asked me to ask a question about AI consciousness.

Speaker 3:
Hi, Adam. Hi, Yann.

Unknown Speaker:
Okay, so you both said, I think, roughly, current AI systems probably not conscious. Future AI systems, possibly descendants of the ones today, but some future AI systems probably will be conscious.

So I guess I want to know, one, what requirements for consciousness do you think current systems are lacking? And then the positive side of that is what steps Do you think we need to tape in order to develop AI systems which are conscious?

And third, when is that going to happen?

Speaker 3:
Okay, I give a crack at this. And David already knows my answer, but So first of all,  I don't attribute like I don't really know how to define consciousness and I don't attribute much importance to it.

And this is an insult to David, I'm sorry. Because he devoted his entire career to it. Okay, that's a different thing. Okay, subjective experience. So clearly, we're going to have systems that have subjective experience that have Emotions.

Emotions, to some extent, are an anticipation of outcome. If we have systems that have world models that are capable of anticipating the outcome of a situation,

 perhaps resulting from their actions, they're going to have emotions because they can predict whether something is going to end up,  you know, good or bad for, you know, on the way to fulfilling their objectives,  right?

So they're going to have all those characteristics. I don't know how to define consciousness in this,

 but perhaps consciousness would be the ability for the system to kind of observe itself and configure itself to solve a particular sub-problem that it's facing.

It needs to have kind of a way of observing itself and configuring itself to solve a particular problem. We certainly can do this. And so perhaps that's what gives us the illusion of consciousness.

I have no doubt this will happen at some point.

Speaker 2:
And will the machines have moral worth when it happens?

Speaker 3:
Yeah, absolutely. I mean, they will have some moral sense. Whether it aligns with us or not will depend on how we define those objectives and guardrails. But yeah, they will have a sense of moral.

Speaker 1:
Let me ask Adam this question a slightly different way, or you can answer the same question as well. Are we too attached to the human subjective experience? Our sense of consciousness.

Clearly, we already know that animals don't have the same experience that we do. And why should we imagine that the superintelligence will have the same subjective experience as human beings?

Speaker 2:
Okay, let me answer all your questions then. Just my gut. I think machines can certainly be conscious in principle,

 that if they're doing at the artificial neurons end up doing the same information Processing in the same way as human neurons,  then at the very least that will give rise to consciousness.

It's not about the substrate, whether it's silicon or carbon,  it's just about the nature of the information processing will give rise to consciousness.

What we're missing to get there, as David knows, there are these things called the neural correlates of consciousness.

People who don't want to say they're studying consciousness directly can look at human brains or perhaps animal brains and say,  what is the processes going on in the neurons that give rise to conscious experience?

There's a number of theories. And from my point of view, they all kind of suck. There's the recurrence theory that you need to be able to take your outputs and plug them back in to the inputs. And that's an essential part of consciousness.

There's something called global workspace theory, integrated information theory. Every physicist and neuroscientists like to have their own There's a set of criteria for what it is for a machine,

 for an information processing system to be conscious. I don't find any of them particularly compelling. And I think we should have extreme humility about recognizing consciousness in other entities. We are very bad at doing it in animals.

We've very much changed our mind over history, whether animals are conscious, whether babies experience consciousness. My question is a little bit, don't know. But I do think that if you just told me about neural networks or told,

 you know, If I didn't know about consciousness,  and I just heard about the processing of information that happens in neural networks,  human neural networks, I would not have predicted that gives rise to consciousness.

That's a great surprise. And we should be, for that reason, extremely humble, even about what the form of the consciousness would make.

To answer Janna's question, we have seen that what we used to think of as a reasonably unified idea of intelligence,  human intelligence, which is a whole bunch of different abilities and And skills.

We've unbundled that with these machine intelligences, where we constructed things that have some of them, but not others. Very superhuman in some, subhuman in others. Perhaps we will be unbundling consciousness as well.

And this thing that we think of as consciousness, we will realise that there is,  you know, many different aspects to it, that we can have some and not the others.

And maybe, as you indicated, we can even transcend Human consciousness in some capacities. I'm pretty excited about answering this question, though.

I think we finally, finally, finally have a model organism for intelligence in the form of these artificial minds that we're building.

And maybe we can turn that model organism for intelligence into a model organism for consciousness and answer some of these questions that have intrigued mankind.

Speaker 3:
I just didn't think I heard an answer to when.

Speaker 2:
I can neither confirm nor deny, I think, is the standard phrase we're using here. I think if progress keeps going.

Speaker 3:
2036. Okay, not in the next two years.

Speaker 1:
Just one closing question. We're a little bit over time, but I'm going to ask this to you, Yann. In many ways, you're a contrarian, maybe not by choice. Maybe this is just how it's happened. You've called it the cult of LLMs.

You sort of often refer to the fact that in Silicon Valley, you don't have the most conventional approach. But yet, you have an optimism. You really do not indulge in the doomsday sort of rhetoric.

What is your most optimistic vision for, if not two years from now, 2036?

Speaker 3:
The new renaissance, that's a pretty optimistic view of, you know, AI systems that amplify human intelligence,  is under our control, can solve a lot of complex problems,  can accelerate the progress of science and medicine,

 can educate our children, you know, help us You know,  process all the information or bring us all the knowledge and information that we need to see.

In fact, you know, people have been interacting with AI systems for much longer than they realize. Of course, there is, you know, LLMs and chatbots now for the last three years.

But before that, you know, most, like every car sold in the EU and most cars sold in In the US have what's called ADAS,  Advanced Driving Assistance Systems or Automatic Emergency Braking Systems. You know,

 a camera that looks out the window and stops your car if you are about to hit a pedestrian or another car. It saves lives. You get an x-ray today, let's say a mammogram or something.

You know, at the bottom it says the thing has been reviewed by an AI system. It saves lives. You can get an MRI now, full-body MRI, in 40 minutes.

This is because you can accelerate the process of collecting the data because AI systems can sort of fill in the blanks. You don't need to collect as much data for this.

But also all the news you're seeing, whether you connect on Google or, you know,  Facebook, Instagram, any social network, is determined by an AI system that basically caters to your interests.

And so, you know, AI has been with us for a while already.

Speaker 1:
But you're saying we should be impressed when they can pour a glass of water and do our dishes.

Speaker 3:
Pour a glass of water, do our dishes, you know, drive our cars,  like learn to drive our cars in 10 hours.

Speaker 1:
Without the cheating.

Speaker 3:
Without all the cheating with sensors and mapping and hard coding of rules. So yeah, this is going to take a while. But this is going to be the next revolution of AI. So this is what I'm working on. Okay.

And, and the message of being, you know, carrying for a while now is, is, okay, LLMs are great. They're useful. We should invest in them. A lot of people are going to use them. They are not a path to human level intelligence. They're just not.

Right now they're sucking the air out of the womb anywhere they go. And so there's basically no resource left for anything else. And so for the next revolution, we need to kind of, you know,

 take a step back and figure out what's missing from current approaches. And then I've been making proposals on this and working inside of Meta for a number of years on this alternative approach.

It's We've come to the point where we need to kind of accelerate this progress now because we know it works. We have early results. That's the pen.

Speaker 1:
OK, I could we could have a whole another hour starting right here. But I hope you'll all join me in thanking our guests for an incredible conversation.

Unknown Speaker:
Thank you so much.

